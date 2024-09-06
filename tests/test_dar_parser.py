# test_dar_parser.py

import unittest
import json
from tools.har_to_dar_converter import convert_har_to_dar


class TestDARParser(unittest.TestCase):

    def setUp(self):
        # Create a sample HAR file for testing
        self.har_file = 'test_input.har'
        self.dar_file = 'test_output.dar'
        self.sample_har_data = {
            "log": {
                "version": "1.2",
                "creator": {
                    "name": "Test Creator",
                    "version": "1.0"
                },
                "pages": [],
                "entries": []
            }
        }

        # Write the sample HAR data to a file
        with open(self.har_file, 'w', encoding='utf-8') as f:
            json.dump(self.sample_har_data, f)

    def test_convert_har_to_dar(self):
        # Run the conversion function
        convert_har_to_dar(self.har_file, self.dar_file)

        # Check if DAR file was created
        with open(self.dar_file, 'r', encoding='utf-8') as f:
            dar_data = json.load(f)

        # Test if renders and result objects are added correctly
        self.assertIn('renders', dar_data['log'], "DAR file missing 'renders' object.")
        self.assertIn('result', dar_data['log'], "DAR file missing 'result' object.")
        self.assertEqual(dar_data['log']['result']['summary'], "Crawl completed successfully",
                         "DAR 'result' object summary is incorrect.")

    def tearDown(self):
        # Clean up test files
        import os
        os.remove(self.har_file)
        os.remove(self.dar_file)


if __name__ == '__main__':
    unittest.main()

