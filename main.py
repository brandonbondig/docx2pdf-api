from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import uvicorn
import os

app = FastAPI()

#standard get

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/convert/")
async def convert_doc_to_pdf(file: UploadFile = File(...)):

    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())

    output_filename = file.filename
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', file.filename])

    output_filename = output_filename.replace(".docx", ".pdf")

    return FileResponse(path=output_filename, filename=output_filename)


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='localhost')