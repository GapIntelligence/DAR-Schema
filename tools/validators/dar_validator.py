# dar_validator.py
"""
DAR Validator

This script validates the structure and content of a DAR (Data Archive Request) file to ensure
compliance with the DAR Schema specification. It checks for required objects, data types, and 
the correct format of the DAR file.
"""

import json
import sys


class DARValidator:
    def __init__(self, file_path):
        """
        Initialize the DARValidator with a specified DAR file.

        :param file_path: Path to the DAR file to be validated.
        """
        self.file_path = file_path
        self.data = self.load_dar_file()

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
        except json.JSONDecodeError:
            print(f"Error: File {self.file_path} is not a valid JSON.")
            raise

    def validate(self):
        """
        Validates the DAR file structure and content.

        :return: A list of validation errors, empty if no errors are found.
        """
        errors = []
        log = self.data.get('log')

        # Validate log object
        if not log:
            errors.append("Missing 'log' object.")
        else:
            # Validate version
            if 'version' not in log or not isinstance(log['version'], str):
                errors.append("Missing or invalid 'version' field in 'log' object.")

            # Validate creator object
            creator = log.get('creator')
            if not creator or 'name' not in creator or 'version' not in creator:
                errors.append("Missing or incomplete 'creator' object in 'log'.")

            # Validate renders object
            renders = log.get('renders')
            if not renders or not isinstance(renders, list):
                errors.append("Missing or invalid 'renders' object; must be a list.")

            # Check each render object
            for i, render in enumerate(renders):
                if not isinstance(render, dict):
                    errors.append(f"Render object at index {i} is not a dictionary.")
                    continue

                if 'url' not in render or not isinstance(render['url'], str):
                    errors.append(f"Missing or invalid 'url' in render object at index {i}.")

                if 'status' not in render or not isinstance(render['status'], str):
                    errors.append(f"Missing or invalid 'status' in render object at index {i}.")

                if 'content' not in render or not isinstance(render['content'], str):
                    errors.append(f"Missing or invalid 'content' in render object at index {i}.")

                if 'time' not in render or not isinstance(render['time'], str):
                    errors.append(f"Missing or invalid 'time' in render object at index {i}.")

            # Validate result object
            result = log.get('result')
            if not result or not isinstance(result, dict):
                errors.append("Missing or invalid 'result' object; must be a dictionary.")
            else:
                if 'summary' not in result or not isinstance(result['summary'], str):
                    errors.append("Missing or invalid 'summary' in 'result' object.")

                # Optional: validate errors array and metrics object
                errors_list = result.get('errors')
                if errors_list and not isinstance(errors_list, list):
                    errors.append("'errors' in 'result' should be a list if present.")

                metrics = result.get('metrics')
                if metrics and not isinstance(metrics, dict):
                    errors.append("'metrics' in 'result' should be a dictionary if present.")

            # Validate entries object
            entries = log.get('entries')
            if not entries or not isinstance(entries, list):
                errors.append("Missing or invalid 'entries' object; must be a list.")

        return errors

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
    if len(sys.argv) != 2:
        print("Usage: python dar_validator.py <path_to_dar_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        validator = DARValidator(file_path)
        validator.print_validation_report()
    except Exception as e:
        print(f"An error occurred: {e}")

