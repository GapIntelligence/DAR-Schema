# DAR Schema Specification

## Introduction

The DAR (Data Archive Request) Schema is an enhanced version of the HAR (HTTP Archive) format, designed to capture a more complete and efficient dataset for web scraping, monitoring, and data collection tasks. DAR files extend the traditional HAR format by introducing new objects such as `renders` and `result`, which provide a richer view of the scraping process.

This document specifies the DAR Schema, describing its structure, key objects, data types, and validation requirements.

## Table of Contents
- [Overview](#overview)
- [Key Differences Between DAR and HAR](#key-differences-between-dar-and-har)
- [DAR File Structure](#dar-file-structure)
  - [Log Object](#log-object)
  - [Renders Object](#renders-object)
  - [Result Object](#result-object)
  - [Entries Object](#entries-object)
- [Encoding Requirements](#encoding-requirements)
- [Sample DAR File](#sample-dar-file)
- [Validation and Compliance](#validation-and-compliance)

## Overview

DAR files are designed to provide:
- **Enhanced Data Collection**: The DAR format captures not just network traffic but also rendering and summary information.
- **Improved Performance**: Optimized for faster, more reliable data handling during large-scale scraping operations.
- **Comprehensive View**: By capturing render pages and summary results, DAR provides insights that go beyond what HAR files can offer.

## Key Differences Between DAR and HAR

1. **New Objects**: DAR introduces `renders` and `result` objects that are not present in HAR files.
2. **Enhanced Data Structure**: DAR files are structured to capture render data for each step of the scraping process.
3. **UTF-8 Encoding Requirement**: Unlike HAR, DAR files must be saved in UTF-8 encoding, ensuring consistent compatibility.

## DAR File Structure

A DAR file is a JSON document structured similarly to HAR, with additional objects and data fields that enhance its utility for web scraping and data archiving.

### Log Object
The root of the DAR file is the `log` object, similar to HAR. It contains metadata about the DAR file, including the version, creator, and the data collected.

- **`version`**: (String) The DAR version. Example: `"1.4"`.
- **`creator`**: (Object) Information about the tool that generated the DAR file.
  - **`name`**: (String) Name of the tool.
  - **`version`**: (String) Version of the tool.
- **`renders`**: (Array) A list of render objects, each representing a captured state of the page during scraping.
- **`result`**: (Object) A summary of the scraping task, including key results and status.
- **`entries`**: (Array) A list of HTTP request/response entries, similar to HAR.

### Renders Object
The `renders` object captures the state of a page at different stages of rendering. This allows for a detailed look at how data was collected and presented during the scrape.

- **`renders`**: (Array of Objects) Each render object represents a single page render captured during the scraping process.
  - **`url`**: (String) The URL of the rendered page.
  - **`status`**: (String) HTTP status code of the page at the time of render.
  - **`content`**: (String) Serialized HTML content or DOM snapshot of the render.
  - **`time`**: (String) Timestamp of when the render was captured in ISO 8601 format.
  - **`image`**: (String, Optional) Base64 encoded PNG image of the rendered page (e.g., screenshots).
  - **`thumb`**: (String, Optional) Base64 encoded thumbnail of the render for quick reference.

### Result Object
The `result` object summarizes the overall outcome of the scraping session, including any errors encountered, data points collected, and the status of the task.

- **`result`**: (Object)
  - **`summary`**: (String) A high-level summary of the scraping process (e.g., "Crawl completed successfully").
  - **`errors`**: (Array, Optional) A list of errors encountered during scraping.
  - **`metrics`**: (Object, Optional) Key performance metrics such as response time, number of requests, etc.

### Entries Object
The `entries` object functions similarly to the HAR entries, capturing HTTP requests and responses during the scraping session.

- **`entries`**: (Array of Objects)
  - Each entry contains details of a single HTTP request and response, including headers, request URL, response status, timing, and other relevant data.

## Encoding Requirements

DAR files must be saved using UTF-8 encoding. Other encodings are not allowed. The use of a BOM (Byte Order Mark) is permitted but not required. 

## Sample DAR File

Here is an example of a minimal DAR file:

```json
{
  "log": {
    "version": "1.4",
    "creator": {
      "name": "OpenBrand DAR Converter",
      "version": "1.0"
    },
    "renders": [
      {
        "url": "https://example.com",
        "status": "200",
        "content": "<html>...</html>",
        "time": "2024-09-05T12:00:00Z",
        "image": "base64-encoded-image-data",
        "thumb": "base64-encoded-thumbnail-data"
      }
    ],
    "result": {
      "summary": "Crawl completed successfully",
      "errors": [],
      "metrics": {
        "requests": 10,
        "renderTime": "2.3s"
      }
    },
    "entries": [
      {
        "request": {
          "method": "GET",
          "url": "https://example.com",
          "headers": []
        },
        "response": {
          "status": 200,
          "statusText": "OK",
          "headers": [],
          "content": {
            "size": 1234,
            "mimeType": "text/html"
          }
        },
        "time": 100
      }
    ]
  }
}
```

## Validation and Compliance

To ensure a DAR file is compliant with this specification:
- Check for the presence of required objects (`log`, `renders`, `result`).
- Validate data types and structures as outlined in this document.
- Use DAR validator tools to automate the compliance process, ensuring consistent adherence to the format.

---

This specification serves as a guide for implementing and using DAR files. As the DAR Schema evolves, updates will be reflected in future versions of this document.
