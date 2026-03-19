"""
Stage 1 + 2: Image triage and nutrient extraction via Claude vision API.

A single API call per image handles both:
- Triage: does the image contain a nutrition/supplement facts panel?
- Extraction: structured list of nutrients if yes.

This is cheaper and faster than two separate calls, and the LLM handles
both decisions simultaneously without any quality loss.
"""

import base64
import json
import re
from pathlib import Path

import anthropic

from nutrition_label_parser.config import MODEL_NAME
from nutrition_label_parser.models import ExtractionResult

_MEDIA_TYPES: dict[str, str] = {
    'png': 'image/png',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
}

_SYSTEM_PROMPT = (
    'You are a nutrition label data extraction specialist. '
    'Your job is to extract structured nutritional data from product label images. '
    'You must always respond with valid JSON — no other text, no markdown explanation, '
    'no code fences. Just the raw JSON object. '
    'Be literal and faithful to what is on the label. '
    'Do not infer, estimate, or hallucinate values. '
    'If a value is not clearly visible, omit it (null) or mark confidence as "low".'
)

_USER_PROMPT = '''Analyse this product label image and extract nutritional information.

Step 1 — Triage: Does this image contain a nutrition facts panel, supplement facts panel, or nutritional information table?
- Count as YES: any structured list of nutrients with amounts (table, paragraph, circular infographic, sidebar)
- Count as NO: front-of-pack images, product photos, ingredient lists only (without amounts), marketing copy, storage instructions, preparation directions

Step 2 — If YES, extract all nutrients listed.

Return ONLY a JSON object with this exact structure:

If the image CONTAINS a nutrition panel:
{
  "has_nutrition_panel": true,
  "skip_reason": null,
  "serving_size": "1 capsule (500mg)",
  "nutrients": [
    {
      "nutrient_name_raw": "Vitamin C",
      "amount": 80.0,
      "unit": "mg",
      "daily_value_pct": 100.0,
      "confidence": "high"
    }
  ]
}

If the image does NOT contain a nutrition panel:
{
  "has_nutrition_panel": false,
  "skip_reason": "Front of pack image, no nutrition table visible",
  "serving_size": null,
  "nutrients": []
}

Extraction rules:
- nutrient_name_raw: Copy the nutrient name EXACTLY as it appears on the label (preserve original capitalisation and special characters). Do NOT translate non-English names.
- amount: Numeric value only (float or null). Do NOT include the unit in this field. If no amount is stated, use null.
- unit: The unit string only (e.g. "mg", "g", "µg", "IU", "kcal"). Do NOT include the numeric value. Use null if no unit is present.
- daily_value_pct: The %DV / %NRV as a float (e.g. 25.0 for "25%"). Use null if not shown.
- confidence: "high" if text is clearly legible, "medium" if partially obscured/inferred from context, "low" if guessing due to blur or rotation.
- serving_size: Copy the serving size string verbatim (e.g. "1 scoop (8.5g)", "2 softgels (1000mg)"). Use null if not present.
- For proprietary blends with sub-items (e.g. "Nootropic Blend 500mg" listing Bacopa 100mg, etc.): extract the blend itself as one row AND each sub-item as its own row. Use null for amount on sub-items that don't list a quantity.
- Extract ALL nutrients, including sub-rows, indented items, and footnotes that list quantified nutrients.
- If the label is in a non-English language, copy nutrient names verbatim in the original language. The amount and unit fields should still be numeric/unit-only.
'''


def triage_and_extract(image_path: Path, api_key: str = '') -> ExtractionResult:
    """
    Send a product label image to Claude and return triage + extraction results.

    Returns ExtractionResult with has_nutrition_panel=False if no panel is found,
    or a populated nutrients list if extraction succeeded.
    """
    client = anthropic.Anthropic(api_key=api_key)
    image_data = _load_image_as_base64(image_path)
    media_type = _get_media_type(image_path)

    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=4096,
        system=_SYSTEM_PROMPT,
        messages=[
            {
                'role': 'user',
                'content': [
                    {
                        'type': 'image',
                        'source': {
                            'type': 'base64',
                            'media_type': media_type,
                            'data': image_data,
                        },
                    },
                    {'type': 'text', 'text': _USER_PROMPT},
                ],
            }
        ],
    )

    raw_text = message.content[0].text  # type: ignore[union-attr]
    return _parse_response(raw_text)


def _load_image_as_base64(path: Path) -> str:
    with open(path, 'rb') as f:
        return base64.standard_b64encode(f.read()).decode('utf-8')


def _get_media_type(path: Path) -> str:
    suffix = path.suffix.lower().lstrip('.')
    return _MEDIA_TYPES.get(suffix, 'image/png')


def _parse_response(raw_text: str) -> ExtractionResult:
    """
    Extract JSON from the LLM response and validate into ExtractionResult.

    Handles the case where the model wraps output in markdown code fences
    despite explicit instructions not to.
    """
    text = raw_text.strip()

    # Strip markdown code fences: ```json ... ``` or ``` ... ```
    text = re.sub(r'^```(?:json)?\s*\n?', '', text, flags=re.MULTILINE)
    text = re.sub(r'\n?```\s*$', '', text, flags=re.MULTILINE)
    text = text.strip()

    # Fallback: if direct parse fails, extract the first {...} block
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r'\{.*\}', raw_text, re.DOTALL)
        if not match:
            raise ValueError(f'No JSON object found in LLM response: {raw_text[:200]}')
        data = json.loads(match.group())

    return ExtractionResult.model_validate(data)
