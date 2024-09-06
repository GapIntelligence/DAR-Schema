# Usage Examples for DAR Schema

## Introduction

The DAR (Data Archive Request) Schema extends the traditional HAR format by introducing enhanced objects that provide a more comprehensive view of the data collection process. This document provides practical usage examples, demonstrating how to create DAR files, parse them, and utilize the additional information they contain.

## Table of Contents
- [Creating a DAR File from HAR](#creating-a-dar-file-from-har)
- [Parsing a DAR File](#parsing-a-dar-file)
- [Extracting Render Data](#extracting-render-data)
- [Analyzing Scraping Results](#analyzing-scraping-results)
- [Using DAR for Web Scraping](#using-dar-for-web-scraping)
- [Error Handling and Metrics](#error-handling-and-metrics)

## Creating a DAR File from HAR

The `har_to_dar_converter.py` script allows you to convert a standard HAR file into a DAR file. This conversion adds the additional `renders` and `result` objects that are unique to DAR, providing a richer dataset for analysis.

### **Example: Converting HAR to DAR**

1. **Prepare your HAR file**: Ensure you have a HAR file generated from your web scraping or browsing session.
2. **Run the conversion script**:

    ```bash
    python tools/har_to_dar_converter.py input.har output.dar
    ```

3. **Check the output DAR file**: The generated DAR file will include enhanced objects such as `renders` and `result`.

### **Sample Code: `har_to_dar_converter.py`**

```python
from tools.har_to_dar_converter import convert_har_to_dar

# Convert a HAR file to DAR format
convert_har_to_dar('sample_input.har', 'sample_output.dar')
```

## Parsing a DAR File

Parsing DAR files is straightforward using the `dar_parser.py` script. This parser allows you to read and validate DAR files, extract key data, and utilize the enhanced objects for deeper insights.

### **Example: Parsing a DAR File**

1. **Create a DAR file or use an existing one**.
2. **Parse the DAR file using the `dar_parser.py` script**:

    ```bash
    python tools/dar_parser.py
    ```

3. **View the parsed data**: The script will output a summary of the DAR file, including the number of renders, summary of results, and number of request entries.

### **Sample Code: Parsing a DAR File**

```python
from tools.dar_parser import DARParser

# Initialize the parser with a DAR file path
parser = DARParser('sample_output.dar')

# Print a summary of the DAR file
parser.print_dar_summary()
```

## Extracting Render Data

DAR files capture multiple render states of a page, allowing you to see how the content changes during the scraping session. This is particularly useful for monitoring dynamic content or understanding how pages are loaded.

### **Example: Extracting Render Objects**

```python
# Extract and print render data
renders = parser.get_renders()
for render in renders:
    print(f"Render URL: {render['url']}")
    print(f"Render Status: {render['status']}")
    print(f"Render Time: {render['time']}")
    print(f"Content Snippet: {render['content'][:100]}...")  # Print first 100 chars of content
```

## Analyzing Scraping Results

The `result` object in a DAR file provides a summary of the scraping session, including performance metrics, errors, and other key insights. This helps you quickly assess the success of your data collection efforts.

### **Example: Analyzing Scraping Results**

```python
# Extract and print result summary
result_summary = parser.get_result_summary()
print(f"Scraping Result Summary: {result_summary}")
```

## Using DAR for Web Scraping

DAR’s enhanced structure makes it ideal for complex scraping tasks, especially when dealing with dynamic or frequently changing content. By capturing render states and summarizing results, DAR provides a comprehensive view that HAR files cannot match.

### **Example: Using DAR in a Scraping Workflow**

1. **Scrape a website using your preferred tool (e.g., Selenium, Puppeteer) and save the session as a HAR file.**
2. **Convert the HAR file to DAR to capture additional render states and results.**
3. **Use the DAR file to analyze page loads, extract specific data points, and diagnose any errors encountered during scraping.**

```python
# Example of integrating DAR into a scraping workflow
import time
from selenium import webdriver
from tools.har_to_dar_converter import convert_har_to_dar

# Set up Selenium to capture HAR
driver = webdriver.Chrome()
driver.get('https://example.com')

# Assume HAR capturing is set up and saved as 'session.har'
time.sleep(2)  # Wait for page load

# Convert the captured HAR to DAR
convert_har_to_dar('session.har', 'session.dar')

# Parse the DAR file and analyze results
parser = DARParser('session.dar')
parser.print_dar_summary()
```

## Error Handling and Metrics

DAR files include detailed error logs and performance metrics that are invaluable for debugging and optimizing your scraping processes. These insights allow you to fine-tune your approach and ensure data quality.

### **Example: Extracting Errors and Metrics**

```python
# Extract errors and performance metrics from the DAR file
errors = parser.data['log']['result'].get('errors', [])
metrics = parser.data['log']['result'].get('metrics', {})

print("Errors Encountered:", errors)
print("Performance Metrics:", metrics)
```

---

These examples demonstrate how DAR can be effectively utilized in a variety of scraping and data collection workflows, providing a more detailed and useful dataset than traditional HAR files. By leveraging DAR’s enhanced capabilities, you can gain deeper insights into your web scraping operations, optimize performance, and ensure more reliable data collection.
