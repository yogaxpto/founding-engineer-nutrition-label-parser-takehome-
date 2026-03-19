"""
Deterministic normalisation for nutrient names and units.
No API calls — fully unit-testable.
"""

import re

from nutrition_label_parser.nutrient_map import NUTRIENT_MAP, UNIT_MAP, NutrientName, Unit


def normalize_nutrient_name(raw: str) -> NutrientName | str:
    """
    Map a raw nutrient name to a standard snake_case identifier.

    Lookup order:
    1. Direct match (case-insensitive, stripped)
    2. Parenthetical stripped: "Vitamin C (Ascorbic Acid)" → "vitamin c"
    3. Fallback: snake_case of the raw name

    The fallback ensures unknown nutrients (e.g. proprietary blends) are
    preserved rather than dropped or silently mis-mapped.
    """
    key = raw.strip().lower()

    if key in NUTRIENT_MAP:
        return NUTRIENT_MAP[key]

    # Strip parenthetical content and retry
    key_stripped = re.sub(r'\s*\(.*?\)', '', key).strip()
    if key_stripped in NUTRIENT_MAP:
        return NUTRIENT_MAP[key_stripped]

    return _to_snake_case(raw.strip())


def normalize_unit(raw: str | None) -> Unit | str | None:
    """
    Map a raw unit string to its canonical form.

    Returns None for None input. Unknown units are passed through unchanged —
    better to preserve an unexpected unit (e.g. 'CFU') than to silently drop it.
    """
    if raw is None:
        return None
    key = raw.strip().lower()
    return UNIT_MAP.get(key, raw.strip())


def _to_snake_case(text: str) -> str:
    """Convert arbitrary text to snake_case for unmapped nutrient names."""
    text = text.lower()
    text = re.sub(r'[\s\-/]+', '_', text)
    text = re.sub(r'[^\w]', '', text)
    text = re.sub(r'_+', '_', text)
    return text.strip('_')
