# Document OCR & Analysis Application

This application uses Google's Gemini AI to perform OCR and analysis on document images. It consists of a FastAPI backend and a Streamlit frontend for a user-friendly interface.

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your Gemini API key: (see .env.example)
```
GEMINI_API_KEY=your_api_key_here
```

## Running the Application

The application consists of two components that need to be running simultaneously:

1. Start the FastAPI backend server:
```bash
python main.py
```
The backend will be available at `http://localhost:8000`

2. In a new terminal window, start the Streamlit frontend:
```bash
streamlit run streamlit_app.py
```
The frontend will be available at `http://localhost:8501`

## Using the Application

1. Open your web browser and navigate to `http://localhost:8501`
2. Upload a document image (supported formats: PNG, JPG, JPEG)
3. Choose your analysis mode:
   - Automatic Information Extraction: Extracts all relevant information from the document
   - Custom Query: Ask specific questions about the document
4. Click "Analyze Document" to process
5. View the results in the right panel

## Features

- Document image upload and preview
- Two analysis modes:
  - Automatic information extraction
  - Custom query support
- Real-time document analysis
- Formatted JSON results display
- Error handling and loading states

## API Endpoints

The backend provides two main endpoints:

- `/submit-document/`: Automatic information extraction
- `/submit-document-text/`: Custom query analysis

## Dependencies

- streamlit==1.32.0
- fastapi==0.110.0
- uvicorn==0.27.1
- python-dotenv==1.0.1
- Pillow==10.2.0
- google-generativeai==0.3.2
- python-multipart==0.0.9
- requests==2.31.0
