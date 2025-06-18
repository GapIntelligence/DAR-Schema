# test_converter.py

import unittest
import json
from tools.har_to_dar_converter import convert_har_to_dar


class TestConverter(unittest.TestCase):

    def setUp(self):
        # Setup test input and output file paths
        self.input_har = 'input_test.har'
        self.output_dar = 'output_test.dar'

        # Example HAR content with a single entry
        har_content = {
            "log": {
                "version": "1.2",
                "creator": {
                    "name": "browser",
                    "version": "1.0"
                },
                "entries": [
                    {
                        "request": {"method": "GET", "url": "https://example.com"},
                        "response": {"status": 200, "statusText": "OK"},
                        "time": 50
                    }
                ]
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

        # Entries should be copied from the HAR file
        self.assertEqual(
            dar_data['log']['entries'][0]['request']['url'],
            "https://example.com"
        )

        # Check 'renders' object
        self.assertIn('renders', dar_data['log'])
        renders = dar_data['log']['renders']
        self.assertEqual(len(renders), 1)
        self.assertEqual(renders[0]['url'], "https://example.com")
        self.assertEqual(renders[0]['status'], "200")
        self.assertIn('time', renders[0])

        # Check 'result' object
        self.assertIn('result', dar_data['log'])
        result = dar_data['log']['result']
        self.assertEqual(result['summary'], "Crawl completed successfully")
        self.assertEqual(result['metrics']['requests'], 1)
        self.assertEqual(result['errors'], [])

    def tearDown(self):
        # Remove test files
        import os
        os.remove(self.input_har)
        os.remove(self.output_dar)


if __name__ == '__main__':
    unittest.main()

