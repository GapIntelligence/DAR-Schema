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
                "entries": [
                    {
                        "request": {"method": "GET", "url": "https://example.com"},
                        "response": {"status": 200, "statusText": "OK"},
                        "time": 75
                    }
                ]
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

        # Entries copied correctly
        self.assertEqual(dar_data['log']['entries'][0]['response']['status'], 200)

        # Validate renders object
        self.assertIn('renders', dar_data['log'])
        renders = dar_data['log']['renders']
        self.assertEqual(len(renders), 1)
        self.assertEqual(renders[0]['url'], "https://example.com")
        self.assertEqual(renders[0]['status'], "200")

        # Validate result object
        self.assertIn('result', dar_data['log'])
        result = dar_data['log']['result']
        self.assertEqual(result['summary'], "Crawl completed successfully")
        self.assertEqual(result['metrics']['requests'], 1)
        self.assertEqual(result['errors'], [])

    def tearDown(self):
        # Clean up test files
        import os
        os.remove(self.har_file)
        os.remove(self.dar_file)


if __name__ == '__main__':
    unittest.main()

