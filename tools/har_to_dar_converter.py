# har_to_dar_converter.py
"""
HAR to DAR Converter

This script converts a standard HAR file to a DAR file, adding the necessary
render and result objects to conform to the DAR schema.
"""

import json
import sys

def convert_har_to_dar(har_file, dar_file):
    try:
        with open(har_file, 'r', encoding='utf-8') as har:
            har_data = json.load(har)

        # Example conversion - add render and result placeholders
        har_data['log']['renders'] = []  # Add render object
        har_data['log']['result'] = {"summary": "Crawl completed successfully"}  # Add result object

        with open(dar_file, 'w', encoding='utf-8') as dar:
            json.dump(har_data, dar, indent=4)

        print(f"Converted {har_file} to {dar_file} successfully.")

    except Exception as e:
        print(f"Error converting {har_file} to {dar_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python har_to_dar_converter.py <input.har> <output.dar>")
    else:
        convert_har_to_dar(sys.argv[1], sys.argv[2])

