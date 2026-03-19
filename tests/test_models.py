from nutrition_label_parser.models import ExtractionResult, NutrientRawExtract, NutrientRow


class TestNutrientRawExtract:
    def test_defaults(self) -> None:
        n = NutrientRawExtract(nutrient_name_raw='Protein')
        assert n.amount is None
        assert n.unit is None
        assert n.daily_value_pct is None
        assert n.confidence == 'high'

    def test_full_row(self) -> None:
        n = NutrientRawExtract(
            nutrient_name_raw='Vitamin C',
            amount=80.0,
            unit='mg',
            daily_value_pct=100.0,
            confidence='medium',
        )
        assert n.amount == 80.0
        assert n.unit == 'mg'
        assert n.daily_value_pct == 100.0

    def test_string_amount_coerced_to_float(self) -> None:
        # LLM sometimes returns "200" (string) instead of 200.0
        n = NutrientRawExtract(nutrient_name_raw='Iron', amount='15')  # type: ignore[arg-type]
        assert n.amount == 15.0

    def test_confidence_literal(self) -> None:
        n = NutrientRawExtract(nutrient_name_raw='X', confidence='low')
        assert n.confidence == 'low'


class TestExtractionResult:
    def test_no_panel_defaults(self) -> None:
        r = ExtractionResult(has_nutrition_panel=False)
        assert r.nutrients == []
        assert r.skip_reason is None
        assert r.serving_size is None

    def test_with_panel(self) -> None:
        r = ExtractionResult(
            has_nutrition_panel=True,
            serving_size='1 scoop (8.5g)',
            nutrients=[NutrientRawExtract(nutrient_name_raw='Protein', amount=20.0, unit='g')],
        )
        assert r.has_nutrition_panel is True
        assert len(r.nutrients) == 1
        assert r.serving_size == '1 scoop (8.5g)'

    def test_model_validate_from_dict(self) -> None:
        data = {
            'has_nutrition_panel': True,
            'serving_size': '2 capsules',
            'nutrients': [
                {'nutrient_name_raw': 'EPA', 'amount': 330, 'unit': 'mg', 'daily_value_pct': None}
            ],
        }
        r = ExtractionResult.model_validate(data)
        assert r.nutrients[0].nutrient_name_raw == 'EPA'
        assert r.nutrients[0].amount == 330.0


class TestNutrientRow:
    def test_model_dump_keys(self) -> None:
        row = NutrientRow(
            product_image='product_01.png',
            nutrient_name_raw='Vitamin C',
            nutrient_name_standard='vitamin_c',
            amount=80.0,
            unit='mg',
            daily_value_pct=100.0,
            serving_size='1 capsule',
            confidence='high',
        )
        d = row.model_dump()
        assert set(d.keys()) == {
            'product_image', 'nutrient_name_raw', 'nutrient_name_standard',
            'amount', 'unit', 'daily_value_pct', 'serving_size', 'confidence',
        }

    def test_nullable_fields_none(self) -> None:
        row = NutrientRow(
            product_image='product_07.jpg',
            nutrient_name_raw='Zinc',
            nutrient_name_standard='zinc',
            amount=None,
            unit=None,
            daily_value_pct=None,
            serving_size=None,
            confidence='low',
        )
        assert row.amount is None
        assert row.unit is None
