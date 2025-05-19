import streamlit as st
import requests
import json
from PIL import Image
import io
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Document OCR & Analysis", page_icon="📄", layout="wide")

st.markdown(
    """
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    .result-box {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📄 Document OCR & Analysis")
st.markdown("""
    Upload a document image and let our AI analyze it for you. You can either:
    - Extract all information automatically
    - Ask specific questions about the document
""")

if "result" not in st.session_state:
    st.session_state.result = None

uploaded_file = st.file_uploader(
    "Choose a document image...", type=["png", "jpg", "jpeg"]
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Document Analysis")

    analysis_mode = st.radio(
        "Choose analysis mode:", ["Automatic Information Extraction", "Custom Query"]
    )

    if analysis_mode == "Custom Query":
        custom_query = st.text_area(
            "Enter your question about the document:",
            placeholder="Example: What is the person's name and date of birth?",
        )

    if uploaded_file is not None:
        if st.button("Analyze Document"):
            with st.spinner("Analyzing document..."):
                files = {"file": (uploaded_file.name, uploaded_file.getvalue())}

                try:
                    if analysis_mode == "Automatic Information Extraction":
                        response = requests.post(
                            "http://localhost:8000/submit-document/", files=files
                        )
                    else:
                        response = requests.post(
                            "http://localhost:8000/submit-document-text/",
                            files=files,
                            data={"prompt": custom_query},
                        )

                    if response.status_code == 200:
                        st.session_state.result = response.json()["result"]
                    else:
                        st.error("Error processing the document. Please try again.")

                except Exception as e:
                    st.error(f"Error: {str(e)}")

with col2:
    st.subheader("🔍 Results")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Document", use_container_width=True)

    if st.session_state.result:
        st.markdown("### Analysis Results")
        try:
            result_json = json.loads(st.session_state.result)
            for key, value in result_json.items():
                st.markdown(f"**{key}:** {value}")
        except:
            st.markdown(st.session_state.result)

st.markdown("---")
st.markdown("Powered by Google Gemini AI")
