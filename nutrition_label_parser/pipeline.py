"""
Stage orchestration: iterate images → extract → normalise → write CSV.
"""

import csv
import logging
from pathlib import Path

from nutrition_label_parser.config import DEFAULT_OUTPUT_PATH
from nutrition_label_parser.extractor import triage_and_extract
from nutrition_label_parser.models import CSV_FIELDNAMES, ExtractionResult, NutrientRow
from nutrition_label_parser.normaliser import normalize_nutrient_name, normalize_unit

logger = logging.getLogger(__name__)

IMAGE_SUFFIXES: set[str] = {'.png', '.jpg', '.jpeg'}


def run_pipeline(
    images_dir: Path,
    output_path: Path = DEFAULT_OUTPUT_PATH,
    api_key: str = '',
) -> None:
    """
    Process all images in images_dir and write normalised rows to output_path CSV.

    - Images are processed in sorted order for deterministic output.
    - Images with no nutrition panel are logged and skipped.
    - Per-image errors are caught and logged; processing continues on the next image.
    """
    image_paths = sorted(p for p in images_dir.iterdir() if p.suffix.lower() in IMAGE_SUFFIXES)

    if not image_paths:
        logger.warning('No images found in %s', images_dir)
        return

    logger.info('Found %d image(s) in %s', len(image_paths), images_dir)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_FIELDNAMES)
        writer.writeheader()

        for image_path in image_paths:
            logger.info('Processing %s', image_path.name)
            try:
                result = triage_and_extract(image_path, api_key=api_key)
            except Exception as exc:
                logger.error('Failed to extract %s: %s', image_path.name, exc)
                continue

            if not result.has_nutrition_panel:
                logger.info('Skipping %s — %s', image_path.name, result.skip_reason)
                continue

            rows = _build_rows(image_path.name, result)
            logger.info('Extracted %d nutrient row(s) from %s', len(rows), image_path.name)
            for row in rows:
                writer.writerow(row.model_dump())

    logger.info('Output written to %s', output_path)


def _build_rows(image_name: str, result: ExtractionResult) -> list[NutrientRow]:
    """Apply normalisation and assemble output rows from an extraction result."""
    rows: list[NutrientRow] = []
    for nutrient in result.nutrients:
        rows.append(
            NutrientRow(
                product_image=image_name,
                nutrient_name_raw=nutrient.nutrient_name_raw,
                nutrient_name_standard=normalize_nutrient_name(nutrient.nutrient_name_raw),
                amount=nutrient.amount,
                unit=normalize_unit(nutrient.unit),
                daily_value_pct=nutrient.daily_value_pct,
                serving_size=result.serving_size,
                confidence=nutrient.confidence,
            )
        )
    return rows
