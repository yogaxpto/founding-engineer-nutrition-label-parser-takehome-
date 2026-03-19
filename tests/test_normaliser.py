from nutrition_label_parser.normaliser import normalize_nutrient_name, normalize_unit
from nutrition_label_parser.nutrient_map import NutrientName, Unit


class TestNormalizeNutrientName:
    def test_direct_match(self) -> None:
        assert normalize_nutrient_name('vitamin c') == 'vitamin_c'

    def test_case_insensitive(self) -> None:
        assert normalize_nutrient_name('Vitamin C') == 'vitamin_c'
        assert normalize_nutrient_name('VITAMIN C') == 'vitamin_c'

    def test_leading_trailing_whitespace(self) -> None:
        assert normalize_nutrient_name('  protein  ') == 'protein'

    def test_alias_ascorbic_acid(self) -> None:
        assert normalize_nutrient_name('Ascorbic Acid') == 'vitamin_c'

    def test_alias_thiamine_mononitrate(self) -> None:
        assert normalize_nutrient_name('Thiamine Mononitrate') == 'vitamin_b1'

    def test_alias_pyridoxine_hcl(self) -> None:
        assert normalize_nutrient_name('Pyridoxine HCL') == 'vitamin_b6'

    def test_alias_epa(self) -> None:
        assert normalize_nutrient_name('Eicosapentaenoic Acid') == 'epa'

    def test_alias_dha(self) -> None:
        assert normalize_nutrient_name('Docosahexaenoic Acid') == 'dha'

    def test_alias_riboflavin(self) -> None:
        assert normalize_nutrient_name('Riboflavin') == 'vitamin_b2'

    def test_alias_folate(self) -> None:
        assert normalize_nutrient_name('Folic Acid') == 'vitamin_b9'

    def test_alias_salt_to_sodium(self) -> None:
        # EU labels use 'salt' for sodium
        assert normalize_nutrient_name('Salt') == 'sodium'

    def test_parenthetical_stripped(self) -> None:
        assert normalize_nutrient_name('Vitamin C (Ascorbic Acid)') == 'vitamin_c'

    def test_parenthetical_with_as_prefix(self) -> None:
        assert normalize_nutrient_name('Folate (as Folic Acid)') == 'vitamin_b9'

    def test_unknown_falls_back_to_snake_case(self) -> None:
        assert normalize_nutrient_name('Synephrine Adaptogenics') == 'synephrine_adaptogenics'

    def test_hyphen_in_unknown(self) -> None:
        assert normalize_nutrient_name('Some-Novel Compound') == 'some_novel_compound'

    def test_l_theanine_known(self) -> None:
        assert normalize_nutrient_name('L-Theanine') == 'l_theanine'

    def test_german_fett(self) -> None:
        assert normalize_nutrient_name('Fett') == 'total_fat'

    def test_german_salz(self) -> None:
        assert normalize_nutrient_name('Salz') == 'sodium'

    def test_german_kohlenhydrate(self) -> None:
        assert normalize_nutrient_name('Kohlenhydrate') == 'total_carbohydrate'

    def test_carbohydrates_alias(self) -> None:
        assert normalize_nutrient_name('Carbohydrates') == 'total_carbohydrate'

    def test_dietary_fibre(self) -> None:
        assert normalize_nutrient_name('Dietary Fibre') == 'dietary_fiber'


class TestNormalizeUnit:
    def test_mg_passthrough(self) -> None:
        assert normalize_unit('mg') == 'mg'

    def test_milligrams_long_form(self) -> None:
        assert normalize_unit('milligrams') == 'mg'
        assert normalize_unit('milligram') == 'mg'

    def test_grams(self) -> None:
        assert normalize_unit('grams') == 'g'
        assert normalize_unit('gram') == 'g'
        assert normalize_unit('g') == 'g'

    def test_micrograms(self) -> None:
        assert normalize_unit('mcg') == 'ug'
        assert normalize_unit('µg') == 'ug'
        assert normalize_unit('micrograms') == 'ug'
        assert normalize_unit('microgram') == 'ug'

    def test_iu_uppercase_preserved(self) -> None:
        assert normalize_unit('iu') == 'IU'
        assert normalize_unit('IU') == 'IU'

    def test_kcal(self) -> None:
        assert normalize_unit('calories') == 'kcal'
        assert normalize_unit('kcal') == 'kcal'
        assert normalize_unit('cal') == 'kcal'

    def test_kj(self) -> None:
        assert normalize_unit('kj') == 'kJ'
        assert normalize_unit('kilojoules') == 'kJ'

    def test_ml(self) -> None:
        assert normalize_unit('ml') == 'mL'
        assert normalize_unit('millilitres') == 'mL'

    def test_none_returns_none(self) -> None:
        assert normalize_unit(None) is None

    def test_unknown_unit_passes_through(self) -> None:
        # e.g. colony-forming units for probiotics
        assert normalize_unit('CFU') == 'CFU'

    def test_empty_string(self) -> None:
        assert normalize_unit('') == ''

    def test_case_insensitive(self) -> None:
        assert normalize_unit('Grams') == 'g'
        assert normalize_unit('GRAMS') == 'g'

    def test_whitespace_stripped(self) -> None:
        assert normalize_unit('  mg  ') == 'mg'


class TestEnumReturnTypes:
    def test_known_nutrient_returns_enum_member(self) -> None:
        assert normalize_nutrient_name('vitamin c') is NutrientName.VITAMIN_C

    def test_known_unit_returns_enum_member(self) -> None:
        assert normalize_unit('mg') is Unit.MG

    def test_unknown_nutrient_returns_plain_str(self) -> None:
        result = normalize_nutrient_name('Synephrine Adaptogenics')
        assert type(result) is str

    def test_unknown_unit_returns_plain_str(self) -> None:
        result = normalize_unit('CFU')
        assert type(result) is str
