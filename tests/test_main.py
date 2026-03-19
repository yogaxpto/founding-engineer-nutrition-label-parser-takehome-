from unittest.mock import patch

from nutrition_label_parser.main import main


class TestMain:
    def test_main(self) -> None:
        with patch('sys.argv', ['nutrition-label-parser', '--api-key', 'sk-test']):
            with patch('nutrition_label_parser.main.run_pipeline') as mock_pipeline:
                main()
                mock_pipeline.assert_called_once()
