"""
Static mapping tables for nutrient name and unit normalisation.

Keys are lowercase, stripped aliases. Values are StrEnum members.
Unknown nutrients fall back to snake_case of the raw name in normaliser.py.
"""

from enum import StrEnum


class NutrientName(StrEnum):
    # Energy
    ENERGY               = 'energy'
    # Macronutrients
    PROTEIN              = 'protein'
    TOTAL_FAT            = 'total_fat'
    SATURATED_FAT        = 'saturated_fat'
    TRANS_FAT            = 'trans_fat'
    MONOUNSATURATED_FAT  = 'monounsaturated_fat'
    POLYUNSATURATED_FAT  = 'polyunsaturated_fat'
    TOTAL_CARBOHYDRATE   = 'total_carbohydrate'
    DIETARY_FIBER        = 'dietary_fiber'
    TOTAL_SUGARS         = 'total_sugars'
    ADDED_SUGARS         = 'added_sugars'
    CHOLESTEROL          = 'cholesterol'
    # Minerals
    SODIUM               = 'sodium'
    CALCIUM              = 'calcium'
    IRON                 = 'iron'
    MAGNESIUM            = 'magnesium'
    ZINC                 = 'zinc'
    SELENIUM             = 'selenium'
    POTASSIUM            = 'potassium'
    PHOSPHORUS           = 'phosphorus'
    IODINE               = 'iodine'
    COPPER               = 'copper'
    MANGANESE            = 'manganese'
    CHROMIUM             = 'chromium'
    MOLYBDENUM           = 'molybdenum'
    CHLORIDE             = 'chloride'
    FLUORIDE             = 'fluoride'
    # Fat-soluble vitamins
    VITAMIN_A            = 'vitamin_a'
    BETA_CAROTENE        = 'beta_carotene'
    VITAMIN_D            = 'vitamin_d'
    VITAMIN_E            = 'vitamin_e'
    VITAMIN_K            = 'vitamin_k'
    VITAMIN_K1           = 'vitamin_k1'
    VITAMIN_K2           = 'vitamin_k2'
    # Water-soluble vitamins
    VITAMIN_C            = 'vitamin_c'
    VITAMIN_B1           = 'vitamin_b1'
    VITAMIN_B2           = 'vitamin_b2'
    VITAMIN_B3           = 'vitamin_b3'
    VITAMIN_B5           = 'vitamin_b5'
    VITAMIN_B6           = 'vitamin_b6'
    VITAMIN_B7           = 'vitamin_b7'
    VITAMIN_B9           = 'vitamin_b9'
    VITAMIN_B12          = 'vitamin_b12'
    CHOLINE              = 'choline'
    INOSITOL             = 'inositol'
    # Omega-3 fatty acids
    OMEGA3_TOTAL         = 'omega3_total'
    EPA                  = 'epa'
    DHA                  = 'dha'
    DPA                  = 'dpa'
    FISH_OIL             = 'fish_oil'
    # Mushroom extracts
    LIONS_MANE_EXTRACT   = 'lions_mane_extract'
    REISHI_EXTRACT       = 'reishi_extract'
    CHAGA_EXTRACT        = 'chaga_extract'
    CORDYCEPS_EXTRACT    = 'cordyceps_extract'
    TURKEY_TAIL_EXTRACT  = 'turkey_tail_extract'
    SHIITAKE_EXTRACT     = 'shiitake_extract'
    MAITAKE_EXTRACT      = 'maitake_extract'
    # Nootropics / adaptogens
    BACOPA_MONNIERI      = 'bacopa_monnieri'
    ASHWAGANDHA          = 'ashwagandha'
    RHODIOLA_ROSEA       = 'rhodiola_rosea'
    GINKGO_BILOBA        = 'ginkgo_biloba'
    L_THEANINE           = 'l_theanine'
    PHOSPHATIDYLSERINE   = 'phosphatidylserine'
    ALPHA_GPC            = 'alpha_gpc'
    L_TYROSINE           = 'l_tyrosine'
    ACETYL_L_CARNITINE   = 'acetyl_l_carnitine'
    HUPERZIA_SERRATA     = 'huperzia_serrata'
    HUPERZINE_A          = 'huperzine_a'
    VINPOCETINE          = 'vinpocetine'


class Unit(StrEnum):
    G    = 'g'
    MG   = 'mg'
    UG   = 'ug'
    KCAL = 'kcal'
    KJ   = 'kJ'
    ML   = 'mL'
    IU   = 'IU'
    PCT  = '%'


NUTRIENT_MAP: dict[str, NutrientName] = {
    # --- Energy ---
    'energy': NutrientName.ENERGY,
    'calories': NutrientName.ENERGY,
    'calorie': NutrientName.ENERGY,
    # --- Macronutrients ---
    'protein': NutrientName.PROTEIN,
    'proteins': NutrientName.PROTEIN,
    'total fat': NutrientName.TOTAL_FAT,
    'fat': NutrientName.TOTAL_FAT,
    'total lipid': NutrientName.TOTAL_FAT,
    'saturated fat': NutrientName.SATURATED_FAT,
    'saturated fatty acids': NutrientName.SATURATED_FAT,
    'saturates': NutrientName.SATURATED_FAT,
    'trans fat': NutrientName.TRANS_FAT,
    'trans fatty acids': NutrientName.TRANS_FAT,
    'trans-fatty acids': NutrientName.TRANS_FAT,
    'monounsaturated fat': NutrientName.MONOUNSATURATED_FAT,
    'monounsaturated fatty acids': NutrientName.MONOUNSATURATED_FAT,
    'monounsaturates': NutrientName.MONOUNSATURATED_FAT,
    'polyunsaturated fat': NutrientName.POLYUNSATURATED_FAT,
    'polyunsaturated fatty acids': NutrientName.POLYUNSATURATED_FAT,
    'polyunsaturates': NutrientName.POLYUNSATURATED_FAT,
    'total carbohydrate': NutrientName.TOTAL_CARBOHYDRATE,
    'total carbohydrates': NutrientName.TOTAL_CARBOHYDRATE,
    'carbohydrates': NutrientName.TOTAL_CARBOHYDRATE,
    'carbohydrate': NutrientName.TOTAL_CARBOHYDRATE,
    'carbs': NutrientName.TOTAL_CARBOHYDRATE,
    'dietary fiber': NutrientName.DIETARY_FIBER,
    'dietary fibre': NutrientName.DIETARY_FIBER,
    'fibre': NutrientName.DIETARY_FIBER,
    'fiber': NutrientName.DIETARY_FIBER,
    'total sugars': NutrientName.TOTAL_SUGARS,
    'sugars': NutrientName.TOTAL_SUGARS,
    'sugar': NutrientName.TOTAL_SUGARS,
    'of which sugars': NutrientName.TOTAL_SUGARS,
    'added sugars': NutrientName.ADDED_SUGARS,
    'cholesterol': NutrientName.CHOLESTEROL,
    # --- Minerals ---
    'sodium': NutrientName.SODIUM,
    'salt': NutrientName.SODIUM,  # EU labels use 'salt' for sodium content
    'calcium': NutrientName.CALCIUM,
    'iron': NutrientName.IRON,
    'magnesium': NutrientName.MAGNESIUM,
    'zinc': NutrientName.ZINC,
    'selenium': NutrientName.SELENIUM,
    'potassium': NutrientName.POTASSIUM,
    'phosphorus': NutrientName.PHOSPHORUS,
    'phosphorous': NutrientName.PHOSPHORUS,
    'iodine': NutrientName.IODINE,
    'copper': NutrientName.COPPER,
    'manganese': NutrientName.MANGANESE,
    'chromium': NutrientName.CHROMIUM,
    'molybdenum': NutrientName.MOLYBDENUM,
    'chloride': NutrientName.CHLORIDE,
    'fluoride': NutrientName.FLUORIDE,
    # --- Fat-soluble vitamins ---
    'vitamin a': NutrientName.VITAMIN_A,
    'retinol': NutrientName.VITAMIN_A,
    'beta-carotene': NutrientName.BETA_CAROTENE,
    'beta carotene': NutrientName.BETA_CAROTENE,
    'vitamin d': NutrientName.VITAMIN_D,
    'vitamin d3': NutrientName.VITAMIN_D,
    'cholecalciferol': NutrientName.VITAMIN_D,
    'vitamin e': NutrientName.VITAMIN_E,
    'tocopherol': NutrientName.VITAMIN_E,
    'alpha-tocopherol': NutrientName.VITAMIN_E,
    'dl-alpha tocopherol': NutrientName.VITAMIN_E,
    'vitamin k': NutrientName.VITAMIN_K,
    'vitamin k1': NutrientName.VITAMIN_K1,
    'phylloquinone': NutrientName.VITAMIN_K1,
    'vitamin k2': NutrientName.VITAMIN_K2,
    'menaquinone': NutrientName.VITAMIN_K2,
    'menaquinone-7': NutrientName.VITAMIN_K2,
    'mk-7': NutrientName.VITAMIN_K2,
    # --- Water-soluble vitamins ---
    'vitamin c': NutrientName.VITAMIN_C,
    'ascorbic acid': NutrientName.VITAMIN_C,
    'l-ascorbic acid': NutrientName.VITAMIN_C,
    'vitamin b1': NutrientName.VITAMIN_B1,
    'thiamine': NutrientName.VITAMIN_B1,
    'thiamin': NutrientName.VITAMIN_B1,
    'thiamine mononitrate': NutrientName.VITAMIN_B1,
    'thiamine hydrochloride': NutrientName.VITAMIN_B1,
    'thiamine hcl': NutrientName.VITAMIN_B1,
    'vitamin b2': NutrientName.VITAMIN_B2,
    'riboflavin': NutrientName.VITAMIN_B2,
    'vitamin b3': NutrientName.VITAMIN_B3,
    'niacin': NutrientName.VITAMIN_B3,
    'nicotinamide': NutrientName.VITAMIN_B3,
    'niacinamide': NutrientName.VITAMIN_B3,
    'nicotinic acid': NutrientName.VITAMIN_B3,
    'vitamin b5': NutrientName.VITAMIN_B5,
    'pantothenic acid': NutrientName.VITAMIN_B5,
    'calcium pantothenate': NutrientName.VITAMIN_B5,
    'vitamin b6': NutrientName.VITAMIN_B6,
    'pyridoxine': NutrientName.VITAMIN_B6,
    'pyridoxine hcl': NutrientName.VITAMIN_B6,
    'pyridoxine hydrochloride': NutrientName.VITAMIN_B6,
    'pyridoxal-5-phosphate': NutrientName.VITAMIN_B6,
    'p-5-p': NutrientName.VITAMIN_B6,
    'vitamin b7': NutrientName.VITAMIN_B7,
    'biotin': NutrientName.VITAMIN_B7,
    'd-biotin': NutrientName.VITAMIN_B7,
    'vitamin b9': NutrientName.VITAMIN_B9,
    'folate': NutrientName.VITAMIN_B9,
    'folic acid': NutrientName.VITAMIN_B9,
    'folacin': NutrientName.VITAMIN_B9,
    'methylfolate': NutrientName.VITAMIN_B9,
    '5-methyltetrahydrofolate': NutrientName.VITAMIN_B9,
    'vitamin b12': NutrientName.VITAMIN_B12,
    'cobalamin': NutrientName.VITAMIN_B12,
    'cyanocobalamin': NutrientName.VITAMIN_B12,
    'methylcobalamin': NutrientName.VITAMIN_B12,
    'adenosylcobalamin': NutrientName.VITAMIN_B12,
    'choline': NutrientName.CHOLINE,
    'choline bitartrate': NutrientName.CHOLINE,
    'inositol': NutrientName.INOSITOL,
    # --- Omega-3 fatty acids (products 11, 12, 13) ---
    'omega-3': NutrientName.OMEGA3_TOTAL,
    'omega 3': NutrientName.OMEGA3_TOTAL,
    'total omega-3': NutrientName.OMEGA3_TOTAL,
    'omega-3 fatty acids': NutrientName.OMEGA3_TOTAL,
    'n-3 fatty acids': NutrientName.OMEGA3_TOTAL,
    'epa': NutrientName.EPA,
    'eicosapentaenoic acid': NutrientName.EPA,
    'dha': NutrientName.DHA,
    'docosahexaenoic acid': NutrientName.DHA,
    'dpa': NutrientName.DPA,
    'docosapentaenoic acid': NutrientName.DPA,
    'fish oil': NutrientName.FISH_OIL,
    'omega-3 fish oil': NutrientName.FISH_OIL,
    # --- Mushroom extracts (product 03) ---
    "lion's mane": NutrientName.LIONS_MANE_EXTRACT,
    'lions mane': NutrientName.LIONS_MANE_EXTRACT,
    "lion's mane extract": NutrientName.LIONS_MANE_EXTRACT,
    'reishi': NutrientName.REISHI_EXTRACT,
    'reishi extract': NutrientName.REISHI_EXTRACT,
    'ganoderma lucidum': NutrientName.REISHI_EXTRACT,
    'chaga': NutrientName.CHAGA_EXTRACT,
    'chaga extract': NutrientName.CHAGA_EXTRACT,
    'inonotus obliquus': NutrientName.CHAGA_EXTRACT,
    'cordyceps': NutrientName.CORDYCEPS_EXTRACT,
    'cordyceps extract': NutrientName.CORDYCEPS_EXTRACT,
    'cordyceps militaris': NutrientName.CORDYCEPS_EXTRACT,
    'turkey tail': NutrientName.TURKEY_TAIL_EXTRACT,
    'turkey tail extract': NutrientName.TURKEY_TAIL_EXTRACT,
    'trametes versicolor': NutrientName.TURKEY_TAIL_EXTRACT,
    'shiitake': NutrientName.SHIITAKE_EXTRACT,
    'shiitake extract': NutrientName.SHIITAKE_EXTRACT,
    'lentinula edodes': NutrientName.SHIITAKE_EXTRACT,
    'maitake': NutrientName.MAITAKE_EXTRACT,
    'maitake extract': NutrientName.MAITAKE_EXTRACT,
    # --- Nootropics / adaptogens (products 01, 10) ---
    'bacopa monnieri': NutrientName.BACOPA_MONNIERI,
    'bacopa': NutrientName.BACOPA_MONNIERI,
    'ashwagandha': NutrientName.ASHWAGANDHA,
    'withania somnifera': NutrientName.ASHWAGANDHA,
    'ksm-66': NutrientName.ASHWAGANDHA,
    'rhodiola rosea': NutrientName.RHODIOLA_ROSEA,
    'rhodiola': NutrientName.RHODIOLA_ROSEA,
    'ginkgo biloba': NutrientName.GINKGO_BILOBA,
    'ginkgo': NutrientName.GINKGO_BILOBA,
    'l-theanine': NutrientName.L_THEANINE,
    'theanine': NutrientName.L_THEANINE,
    'phosphatidylserine': NutrientName.PHOSPHATIDYLSERINE,
    'ps': NutrientName.PHOSPHATIDYLSERINE,
    'alpha-gpc': NutrientName.ALPHA_GPC,
    'alpha gpc': NutrientName.ALPHA_GPC,
    'l-tyrosine': NutrientName.L_TYROSINE,
    'tyrosine': NutrientName.L_TYROSINE,
    'n-acetyl l-tyrosine': NutrientName.L_TYROSINE,
    'acetyl-l-carnitine': NutrientName.ACETYL_L_CARNITINE,
    'alcar': NutrientName.ACETYL_L_CARNITINE,
    'huperzia serrata': NutrientName.HUPERZIA_SERRATA,
    'huperzine a': NutrientName.HUPERZINE_A,
    'vinpocetine': NutrientName.VINPOCETINE,
    # --- German aliases (product 13) ---
    'energie': NutrientName.ENERGY,
    'eiweiß': NutrientName.PROTEIN,
    'fett': NutrientName.TOTAL_FAT,
    'gesättigte fettsäuren': NutrientName.SATURATED_FAT,
    'davon gesättigte fettsäuren': NutrientName.SATURATED_FAT,
    'kohlenhydrate': NutrientName.TOTAL_CARBOHYDRATE,
    'davon zucker': NutrientName.TOTAL_SUGARS,
    'ballaststoffe': NutrientName.DIETARY_FIBER,
    'salz': NutrientName.SODIUM,
    'fischöl': NutrientName.FISH_OIL,
    'fischol': NutrientName.FISH_OIL,
    'omega-3-fettsäuren': NutrientName.OMEGA3_TOTAL,
    'omega-3 fettsäuren': NutrientName.OMEGA3_TOTAL,
    'eicosapentaensäure': NutrientName.EPA,
    'docosahexaensäure': NutrientName.DHA,
}

UNIT_MAP: dict[str, Unit] = {
    # Weight
    'g': Unit.G,
    'gram': Unit.G,
    'grams': Unit.G,
    'mg': Unit.MG,
    'milligram': Unit.MG,
    'milligrams': Unit.MG,
    'ug': Unit.UG,
    'µg': Unit.UG,
    'μg': Unit.UG,
    'mcg': Unit.UG,
    'microgram': Unit.UG,
    'micrograms': Unit.UG,
    # Energy
    'kcal': Unit.KCAL,
    'cal': Unit.KCAL,
    'calorie': Unit.KCAL,
    'calories': Unit.KCAL,
    'kj': Unit.KJ,
    'kilojoule': Unit.KJ,
    'kilojoules': Unit.KJ,
    # Volume
    'ml': Unit.ML,
    'milliliter': Unit.ML,
    'milliliters': Unit.ML,
    'millilitre': Unit.ML,
    'millilitres': Unit.ML,
    # Biological units
    'iu': Unit.IU,
    # Percentage
    '%': Unit.PCT,
}
