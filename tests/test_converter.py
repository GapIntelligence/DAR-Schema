# test_converter.py

import unittest
import json
from tools.har_to_dar_converter import convert_har_to_dar


class TestConverter(unittest.TestCase):

    def setUp(self):
        # Setup test input and output file paths
        self.input_har = 'input_test.har'
        self.output_dar = 'output_test.dar'

        # Example HAR content
        har_content = {
            "log": {
                "version": "1.2",
                "creator": {
                    "name": "browser",
                    "version": "1.0"
                },
                "entries": []
            }
        }

        # Write sample HAR content to file
        with open(self.input_har, 'w') as har_file:
            json.dump(har_content, har_file)

    def test_har_to_dar_conversion(self):
        # Convert HAR to DAR
        convert_har_to_dar(self.input_har, self.output_dar)

        # Load the output DAR file
        with open(self.output_dar, 'r') as dar_file:
            dar_data = json.load(dar_file)

        # Check if 'renders' object exists
        self.assertIn('renders', dar_data['log'])
        self.assertIsInstance(dar_data['log']['renders'], list)

        # Check if 'result' object exists
        self.assertIn('result', dar_data['log'])
        self.assertEqual(dar_data['log']['result'], {
            "summary": "Crawl completed successfully"
        })

    def tearDown(self):
        # Remove test files
        import os
        os.remove(self.input_har)
        os.remove(self.output_dar)


if __name__ == '__main__':
    unittest.main()

