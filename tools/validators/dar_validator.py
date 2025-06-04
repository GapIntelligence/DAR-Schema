# dar_validator.py
"""
DAR Validator

This script validates the structure and content of a DAR (Data Archive Request) file to ensure
compliance with the DAR Schema specification. It checks for required objects, data types, and 
the correct format of the DAR file.
"""

import json
import os
import sys
from jsonschema import Draft7Validator


class DARValidator:
    def __init__(self, file_path, schema_path=None):
        """
        Initialize the DARValidator with a specified DAR file.

        :param file_path: Path to the DAR file to be validated.
        """
        self.file_path = file_path
        self.schema_path = schema_path or os.path.join(os.path.dirname(__file__), '..', '..', 'dar.schema.json')
        self.data = self.load_dar_file()
        self.schema = self.load_schema()

    def load_dar_file(self):
        """
        Loads the DAR file and parses the JSON content.

        :return: Parsed JSON object of the DAR file.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found.")
            raise

    def load_schema(self):
        """Loads the JSON Schema used for DAR validation."""
        try:
            schema_path = os.path.abspath(self.schema_path)
            with open(schema_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: Schema file {self.schema_path} not found.")
            raise
        except json.JSONDecodeError:
            print(f"Error: Schema file {self.schema_path} is not a valid JSON.")
            raise

    def validate(self):
        """
        Validates the DAR file structure and content.

        :return: A list of validation errors, empty if no errors are found.
        """
        validator = Draft7Validator(self.schema)
        return [err.message for err in validator.iter_errors(self.data)]

    def print_validation_report(self):
        """
        Prints the validation report for the DAR file.
        """
        errors = self.validate()
        if errors:
            print("Validation failed with the following errors:")
            for error in errors:
                print(f"- {error}")
        else:
            print("DAR file is valid and conforms to the schema.")


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python dar_validator.py <path_to_dar_file> [schema.json]")
        sys.exit(1)

    file_path = sys.argv[1]
    schema_path = sys.argv[2] if len(sys.argv) == 3 else None
    try:
        validator = DARValidator(file_path, schema_path)
        validator.print_validation_report()
    except Exception as e:
        print(f"An error occurred: {e}")

