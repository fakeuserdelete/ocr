import os
from fastapi import FastAPI, UploadFile, File, Form
from dotenv import load_dotenv
import uvicorn
from api import init_api, get_gemini_response, get_gemini_response_query


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai, model = init_api(API_KEY)

app = FastAPI()

@app.post("/submit-document/")
async def upload_image(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    
    with open(file_location, "wb") as f:
        f.write(await file.read())

    response = get_gemini_response(genai, model, file_location)

    if response:
        try:
            return {"result": response.text}
        except Exception as e:
            return {"error": f"Failed to parse response: {e}"}
    else:
        return {"error": "Failed to get a response from the model"}


@app.post("/submit-document-text/")
async def upload_image_and_text(
    file: UploadFile = File(...),
    prompt: str = Form(...)
):
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())

    custom_prompt = f"Analyze this image, think through it and extract all the information you can find in the image and return it in a structured JSON format. {prompt}"

    response = get_gemini_response_query(genai, model, file_location, custom_prompt)

    if response:
        try:
            return {"result": response.text}
        except Exception as e:
            return {"error": f"Failed to parse response: {e}"}
    else:
        return {"error": "Failed to get a response from the model"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
