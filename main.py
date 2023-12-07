from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import uvicorn
import os
import shutil

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

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
    if os.path.exists(input_filename):
        os.remove(input_filename)

    # Return the converted file
    return FileResponse(path=output_filename, filename=output_filename)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')
