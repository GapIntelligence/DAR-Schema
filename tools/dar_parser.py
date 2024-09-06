# dar_parser.py
"""
DAR Parser

This script provides functions to parse, validate, and extract data from DAR (Data Archive Request) files.
It is designed to help developers work with the DAR format, which extends the traditional HAR format
with additional objects such as 'renders' and 'result'.
"""

import json


class DARParser:
    def __init__(self, file_path):
        """
        Initialize the DARParser with a specified DAR file.

        :param file_path: Path to the DAR file to be parsed.
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
                self.validate_dar_structure(data)
                return data
        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found.")
            raise
        except json.JSONDecodeError:
            print(f"Error: File {self.file_path} is not a valid JSON.")
            raise

    def validate_dar_structure(self, data):
        """
        Validates that the DAR file has the correct structure.

        :param data: Parsed DAR JSON data.
        :raises ValueError: If the structure is incorrect.
        """
        if 'log' not in data:
            raise ValueError("Invalid DAR file: Missing 'log' object.")

        log = data['log']
        if 'renders' not in log or not isinstance(log['renders'], list):
            raise ValueError("Invalid DAR file: 'renders' object missing or not a list.")

        if 'result' not in log or not isinstance(log['result'], dict):
            raise ValueError("Invalid DAR file: 'result' object missing or not a dictionary.")

    def get_renders(self):
        """
        Extracts the 'renders' object from the DAR file.

        :return: List of render objects.
        """
        return self.data['log'].get('renders', [])

    def get_result_summary(self):
        """
        Extracts the summary from the 'result' object in the DAR file.

        :return: Summary string from the result object.
        """
        return self.data['log']['result'].get('summary', 'No summary available.')

    def get_request_entries(self):
        """
        Extracts HTTP request entries from the DAR file.

        :return: List of request entries.
        """
        return self.data['log'].get('entries', [])

    def print_dar_summary(self):
        """
        Prints a summary of the DAR file, including the number of renders and key results.
        """
        print(f"DAR File: {self.file_path}")
        print(f"Number of Renders: {len(self.get_renders())}")
        print(f"Result Summary: {self.get_result_summary()}")
        print(f"Number of Request Entries: {len(self.get_request_entries())}")


if __name__ == "__main__":
    # Example usage
    file_path = input("Enter the path to your DAR file: ")
    try:
        parser = DARParser(file_path)
        parser.print_dar_summary()
    except Exception as e:
        print(f"An error occurred: {e}")

