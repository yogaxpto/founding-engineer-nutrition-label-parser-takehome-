import argparse
import logging
from pathlib import Path

from nutrition_label_parser import config
from nutrition_label_parser.config import DEFAULT_IMAGES_DIR, DEFAULT_OUTPUT_PATH
from nutrition_label_parser.pipeline import run_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Parse product nutrition label images into a normalised CSV.',
    )
    parser.add_argument(
        '--images-dir',
        type=Path,
        default=DEFAULT_IMAGES_DIR,
        help=f'Directory containing product label images (default: {DEFAULT_IMAGES_DIR})',
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help=f'Output CSV file path (default: {DEFAULT_OUTPUT_PATH})',
    )
    parser.add_argument(
        '--api-key',
        default=None,
        help='Anthropic API key (overrides ANTHROPIC_API_KEY env var)',
    )
    parser.add_argument(
        '--log-level',
        default='INFO',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        help='Logging verbosity (default: INFO)',
    )
    args = parser.parse_args()

    api_key = args.api_key or config.ANTHROPIC_API_KEY
    if not api_key:
        parser.error('API key required: pass --api-key or set ANTHROPIC_API_KEY env var')

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    )

    run_pipeline(images_dir=args.images_dir, output_path=args.output, api_key=api_key)


if __name__ == '__main__':
    main()
