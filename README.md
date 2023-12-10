# Docx2PDF API Readme

## Overview
The Docx2PDF API is a FastAPI application designed to convert DOCX files to PDF format. It provides a simple and efficient way to handle file conversion in a web environment.

## Features
- **File Conversion**: Converts DOCX files to PDF.
- **REST API**: Easy to integrate with other applications using HTTP requests.
- **Cross-Origin Resource Sharing (CORS)**: Configured to allow requests from any origin.
- **Asynchronous Handling**: Processes file uploads and conversions asynchronously for better performance.

## Requirements
- Python 3.6 or higher
- FastAPI
- Uvicorn for running the server
- LibreOffice installed on the server for file conversion

## Installation
1. Install the required Python packages:
   ```bash
   pip install fastapi uvicorn
   ```
2. Ensure LibreOffice is installed on your server.

## Usage
1. Start the FastAPI server:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8001
   ```
2. Use the `/convert/` endpoint to upload a DOCX file and receive a converted PDF in response.

### Endpoint Details
- **URL**: `/convert/`
- **Method**: POST
- **Body**: 
  - `doc_file`: The DOCX file to be converted.

## Example
```python
import requests

url = 'http://localhost:8001/convert/'
files = {'doc_file': open('yourfile.docx', 'rb')}
response = requests.post(url, files=files)

with open('output.pdf', 'wb') as f:
    f.write(response.content)
```

## Error Handling
- The API handles file-related errors and ensures the temporary files are cleaned up after conversion.

## Security Notes
- This API does not implement authentication or encryption. Consider adding these features for production use.

## Limitations
- The API currently only supports DOCX to PDF conversion.

## Contribution
Contributions to the project are welcome. Please follow standard GitHub pull request procedures for contributions.

---

Feel free to modify or extend this readme as needed for your application's documentation.