# har_to_dar_converter.py
"""
HAR to DAR Converter

This script converts a standard HAR file to a DAR file, adding the necessary
render and result objects to conform to the DAR schema.
"""

import json
import sys
from datetime import datetime

def convert_har_to_dar(har_file, dar_file):
    try:
        with open(har_file, "r", encoding="utf-8") as har:
            har_data = json.load(har)

        # Copy existing log data from the HAR file
        log = har_data.get("log", {})

        # Ensure entries exist even if empty
        entries = log.get("entries", [])
        log["entries"] = entries

        # Populate a simple render object using the first entry data if available
        first_entry = entries[0] if entries else {}
        render = {
            "url": first_entry.get("request", {}).get("url", ""),
            "status": str(first_entry.get("response", {}).get("status", "")),
            "content": "",
            "time": datetime.utcnow().isoformat() + "Z",
        }
        log["renders"] = [render]

        # Create a structured result object with metrics
        result = {
            "summary": "Crawl completed successfully",
            "errors": [],
            "metrics": {"requests": len(entries)},
        }
        log["result"] = result

        har_data["log"] = log

        with open(dar_file, "w", encoding="utf-8") as dar:
            json.dump(har_data, dar, indent=4)

        print(f"Converted {har_file} to {dar_file} successfully.")

    except Exception as e:
        print(f"Error converting {har_file} to {dar_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python har_to_dar_converter.py <input.har> <output.dar>")
    else:
        convert_har_to_dar(sys.argv[1], sys.argv[2])

