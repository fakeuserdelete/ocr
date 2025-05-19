import google.generativeai as genai
from PIL import Image


def init_api(API_KEY):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    return genai, model


def get_gemini_response(genai, model, image_data, max_retries=5, delay=2):
    retries = 0
    while retries < max_retries:
        try:
            image = Image.open(image_data)
            response = model.generate_content(
                [
                    "Analyze this image, think through it and extract all the information you can find in the image and return it in a structured JSON format.",
                    image,
                ]
            )
            return response
        except Exception as e:
            print(f"Error: {e}")
            retries += 1


def get_gemini_response_query(genai, model, image_data, query, max_retries=5, delay=2):
    retries = 0
    while retries < max_retries:
        try:
            image = Image.open(image_data)
            response = model.generate_content([query, image])
            return response
        except Exception as e:
            print(f"Error: {e}")
            retries += 1
