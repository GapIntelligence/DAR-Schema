# Getting Started with DAR Schema

## Introduction

The DAR (Data Archive Request) Schema is an advanced file format designed to capture a more comprehensive dataset than traditional HAR files. By extending the HAR format with additional objects, DAR provides a richer, more detailed view of the web scraping and data collection process.

This guide will help you get started with DAR by walking you through the installation, basic usage, and integration of DAR tools into your data workflows.

## Table of Contents
- [Installation](#installation)
- [Setting Up Your Environment](#setting-up-your-environment)
- [Creating Your First DAR File](#creating-your-first-dar-file)
- [Parsing and Analyzing DAR Files](#parsing-and-analyzing-dar-files)
- [Integrating DAR in Your Scraping Workflow](#integrating-dar-in-your-scraping-workflow)
- [Next Steps](#next-steps)

## Installation

### 1. Clone the DAR-Schema Repository

Start by cloning the DAR-Schema repository from GitHub:

```bash
git clone https://github.com/OpenBrand/DAR-Schema.git
cd DAR-Schema
```

### 2. Install Required Dependencies

The DAR tools rely on Python, so ensure you have Python installed on your system. You can check if Python is installed by running:

```bash
python --version
```

If Python is not installed, you can download it from [Python's official website](https://www.python.org/downloads/).

Next, install the required Python packages:

```bash
pip install -r requirements.txt
```

This command installs dependencies that are required for running the DAR conversion and parsing scripts.

## Setting Up Your Environment

### 1. Verify Your Setup

After installation, verify that the tools are working correctly by running the help command for the DAR tools:

```bash
python tools/har_to_dar_converter.py --help
```

You should see usage instructions, confirming that the environment is set up correctly.

## Creating Your First DAR File

### Step 1: Generate a HAR File

Before creating a DAR file, you need a HAR file generated from a web scraping session. Most modern browsers and tools like Selenium can export network activity as a HAR file. 

Here’s a simple example using Chrome DevTools:
1. Open Chrome DevTools (`F12` or right-click > Inspect).
2. Go to the **Network** tab.
3. Perform the web interactions you want to capture.
4. Right-click in the Network tab and select **Save all as HAR with content**.

Save this HAR file in your project directory.

### Step 2: Convert HAR to DAR

Use the `har_to_dar_converter.py` script to convert your HAR file into a DAR file.

```bash
python tools/har_to_dar_converter.py input.har output.dar
```

This command will create a DAR file (`output.dar`) from your HAR file (`input.har`), adding enhanced objects like `renders` and `result`.

## Parsing and Analyzing DAR Files

Once you have your DAR file, you can use the `dar_parser.py` tool to read and analyze the data.

### Step 1: Parse the DAR File

Run the `dar_parser.py` script to parse the DAR file and extract key information.

```bash
python tools/dar_parser.py
```

### Step 2: View the Parsed Data

The script will prompt you for the path to your DAR file and output a summary, including:
- Number of renders captured.
- Summary of scraping results.
- Number of HTTP request entries.

### Example Code: Using `dar_parser.py`

```python
from tools.dar_parser import DARParser

# Initialize the parser with your DAR file
parser = DARParser('output.dar')

# Print a detailed summary of the DAR file
parser.print_dar_summary()
```

## Integrating DAR in Your Scraping Workflow

DAR is especially useful when integrated into web scraping workflows, providing insights into how pages are loaded and data is collected. Here’s how you can incorporate DAR into your existing scraping setup.

### Step 1: Scrape a Website

Use Selenium or your preferred tool to navigate and interact with a webpage, capturing a HAR file as you go.

```python
from selenium import webdriver

# Set up Selenium to capture network traffic
driver = webdriver.Chrome()
driver.get('https://example.com')
# Capture the session as HAR (specific to your setup)
```

### Step 2: Convert the HAR File to DAR

After capturing the HAR file, convert it to DAR to enhance the captured data with renders and results.

```bash
python tools/har_to_dar_converter.py session.har session.dar
```

### Step 3: Analyze the DAR File

Use the DAR file to gain insights into your scraping process, identify any errors, and understand how the data was collected.

```python
# Parse and print the summary of your DAR file
parser = DARParser('session.dar')
parser.print_dar_summary()
```

## Next Steps

Now that you’ve created, parsed, and analyzed your first DAR file, you can explore further by:
- Experimenting with additional render states to capture more detailed data.
- Customizing the `result` object to include specific metrics and error handling relevant to your workflow.
- Integrating DAR files into automated data pipelines for monitoring and auditing purposes.

For more advanced usage, check out the [Usage Examples](usage-examples.md) document to explore various ways to utilize DAR in your projects.

---

DAR provides a powerful, flexible way to enhance your data collection processes. By extending HAR with additional render and result data, DAR helps you gain deeper insights and ensure reliable, comprehensive data capture.
