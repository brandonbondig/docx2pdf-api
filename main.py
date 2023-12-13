from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware

import os
import shutil
import subprocess
import uvicorn

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/convert/")
async def convert_doc_to_pdf(doc_file: UploadFile = File(...)):
    
    # Generate unique filenames for input and output
    input_filename = f"input_{os.urandom(6).hex()}.docx"
    output_filename = input_filename.replace(".docx", ".pdf")

    # Save the uploaded DOCX file
    with open(input_filename, "wb") as file:
        shutil.copyfileobj(doc_file.file, file)

    # Convert the file to PDF
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', input_filename])

    # Remove the input file after conversion
    os.remove(input_filename)

    # Read the PDF into memory
    with open(output_filename, 'rb') as file:
        pdf_content = file.read()
    
    try:
        os.remove(output_filename)
    except OSError as e:
        print(f"Error: {e.strerror}")


    # Return the PDF content as a response
    return Response(content=pdf_content, media_type='application/pdf')

if __name__ == '__main__':
    uvicorn.run(app, port=8001)
