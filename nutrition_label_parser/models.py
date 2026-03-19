from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from nutrition_label_parser.nutrient_map import NutrientName, Unit


class NutrientRawExtract(BaseModel):
    """Single nutrient row as returned by the LLM, before normalisation."""

    model_config = ConfigDict(strict=False)  # allow string→float coercion from LLM

    nutrient_name_raw: str
    amount: float | None = None
    unit: str | None = None
    daily_value_pct: float | None = None
    confidence: Literal['high', 'medium', 'low'] = 'high'


class ExtractionResult(BaseModel):
    """Full result for one image from the LLM (triage + extraction combined)."""

    has_nutrition_panel: bool
    skip_reason: str | None = None
    serving_size: str | None = None
    nutrients: list[NutrientRawExtract] = Field(default_factory=list)


class NutrientRow(BaseModel):
    """One row in the output CSV — fully normalised."""

    product_image: str
    nutrient_name_raw: str
    nutrient_name_standard: NutrientName | str
    amount: float | None
    unit: Unit | str | None
    daily_value_pct: float | None
    serving_size: str | None
    confidence: Literal['high', 'medium', 'low']


CSV_FIELDNAMES: list[str] = [
    'product_image',
    'nutrient_name_raw',
    'nutrient_name_standard',
    'amount',
    'unit',
    'daily_value_pct',
    'serving_size',
    'confidence',
]
