# DAR Schema (Data Archive Request)

The **DAR Schema** (Data Archive Request) is an open-source enhancement of the standard HAR (HTTP Archive) file format. Designed to be faster, more reliable, and more comprehensive, DAR files extend the capabilities of HAR, making them ideal for web scraping, monitoring, and data collection tasks.

## **Overview**

### What is a DAR File?
A DAR file builds upon the structure of a HAR file, introducing additional objects such as `renders` and `result` that provide a richer and more complete view of the data collection process. Unlike HAR files, which primarily log HTTP requests and responses, DAR files capture the entire rendering and result of the web scraping task, making them a superior choice for advanced data analysis and archiving.

### Key Differences Between DAR and HAR
- **Enhanced Data Objects**: DAR introduces new objects like `renders` to capture multiple render pages and `result` to summarize the data collection.
- **Optimized Performance**: DAR files are designed to be faster and more efficient in handling large-scale data scraping operations.
- **UTF-8 Encoding Requirement**: Ensures consistency and broad compatibility across different tools and platforms.

## **Features**

- **Multiple Render Pages**: The `renders` object captures data from multiple render passes, providing deeper insights into how data is collected.
- **Result Summaries**: The `result` object provides a high-level summary of the scraping task, including status, data points collected, and any errors encountered.
- **Standardized Encoding**: All DAR files must be UTF-8 encoded, ensuring they work seamlessly across different systems and languages.

## **Why Use DAR?**

1. **Enhanced Data Collection**: Go beyond basic request-response logging with detailed render and result objects that provide a complete picture of the scraping task.
2. **Improved Reliability**: DAR files are built to handle more complex scraping scenarios, reducing errors and providing more robust data logging.
3. **Future-Proof Design**: The DAR format is designed with future needs in mind, supporting advanced data collection techniques that HAR cannot handle.

## **Getting Started**

### Installation

To use the DAR Schema tools and converters, you'll need Python installed on your system. Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/OpenBrand/DAR-Schema.git
cd DAR-Schema
```

### Usage

#### Converting HAR to DAR

The `tools/har_to_dar_converter.py` script allows you to convert a standard HAR file into a DAR file, adding the enhanced render and result objects:

```bash
python tools/har_to_dar_converter.py input.har output.dar
```

### Examples

Check the `samples/` directory for example DAR files that demonstrate the extended capabilities of this format. Sample files include real-world use cases to help you get started quickly.

## **DAR Schema Specification**

### DAR Data Structure

DAR files consist of several key objects:
- **`log`**: The root object, similar to HAR, which contains all exported data.
- **`renders`**: A list of render pages captured during the scraping process. Each render object contains a snapshot of the page data at a specific time.
- **`result`**: A summary object detailing the outcome of the scraping task, including key metrics and any errors encountered.

### Full Specification

For a detailed look at the DAR Schema, see the [SPEC.md](SPEC.md) file in the root directory. This document provides in-depth information on the data structure, encoding requirements, and best practices for using DAR files.

## **Documentation**

- **[Getting Started Guide](docs/getting-started.md)**: A step-by-step guide on setting up and using DAR files.
- **[Comparison with HAR](docs/comparison-with-HAR.md)**: Learn how DAR files improve upon traditional HAR files.
- **[Usage Examples](docs/usage-examples.md)**: Explore practical examples of how to use DAR in various scenarios.

## **Contributing**

We welcome contributions to the DAR Schema! If you have suggestions, bug reports, or want to contribute code, please review our [Contributing Guide](CONTRIBUTING.md) and submit a pull request.

### How to Contribute
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## **Community and Support**

Join the conversation and get support from the community:
- **GitHub Discussions**: Use the Discussions tab to ask questions, share ideas, and get help from other users.
- **Report Issues**: Found a bug? Let us know by opening an issue in the repository.

## **Stay Updated**

- **Follow Us**: Stay up-to-date with the latest news and updates by following our GitHub page.
- **Spread the Word**: Help us grow the DAR community by sharing the project with your network.

---

Thank you for your interest in DAR Schema! We look forward to your feedback and contributions to make DAR the new standard for enhanced data collection.

