import os
from pathlib import Path

ANTHROPIC_API_KEY: str = os.getenv('ANTHROPIC_API_KEY', '')

MODEL_NAME: str = 'claude-sonnet-4-6'

DEFAULT_IMAGES_DIR: Path = Path('Sample_images')
DEFAULT_OUTPUT_PATH: Path = Path('output/nutrition_data.csv')
