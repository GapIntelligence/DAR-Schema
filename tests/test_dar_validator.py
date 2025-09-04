import unittest
import json
import os

from tools.validators.dar_validator import DARValidator


class TestDARValidator(unittest.TestCase):
    def setUp(self):
        self.valid_file = 'valid_test.dar'
        self.invalid_file = 'invalid_test.dar'

        valid_dar = {
            "log": {
                "version": "1.0",
                "creator": {"name": "tester", "version": "1"},
                "renders": [
                    {
                        "url": "https://example.com",
                        "status": "200",
                        "content": "<html></html>",
                        "time": "2024-01-01T00:00:00Z"
                    }
                ],
                "result": {"summary": "ok"},
                "entries": [
                    {"request": {}, "response": {}, "time": 0}
                ]
            }
        }

        invalid_dar = {
            "log": {
                "version": 1.0,
                "creator": {"name": "tester"},
                "renders": "notalist",
                "result": {"summary": 123},
                "entries": "notalist"
            }
        }

        with open(self.valid_file, 'w', encoding='utf-8') as f:
            json.dump(valid_dar, f)

        with open(self.invalid_file, 'w', encoding='utf-8') as f:
            json.dump(invalid_dar, f)

    def tearDown(self):
        os.remove(self.valid_file)
        os.remove(self.invalid_file)

    def test_validate_correct_dar(self):
        validator = DARValidator(self.valid_file)
        errors = validator.validate()
        self.assertEqual(errors, [])

    def test_validate_malformed_dar(self):
        validator = DARValidator(self.invalid_file)
        errors = validator.validate()
        self.assertGreater(len(errors), 0)


if __name__ == '__main__':
    unittest.main()
