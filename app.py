import streamlit as st
import google.generativeai as genai
from PIL import Image
import PyPDF2

# --- Page Configuration ---
st.set_page_config(page_title="OmniQuiz | Bespoke", layout="wide")

# --- High-Contrast Luxury Styling ---
st.markdown("""
    <style>
    .stApp { 
        background: #FFFFFF !important; 
    }
    .main-container {
        background: #FFFFFF;
        padding: 50px;
        max-width: 800px;
        margin: auto;
        color: #111111 !important;
    }
    h1, h2, h3, p, div, label, .stMarkdown, .stWrite { 
        color: #111111 !important; 
    }
    textarea { 
        background: #F9F9F9 !important; 
        color: #000000 !important; 
        border: 1px solid #000 !important;
    }
    .stButton>button {
        background: #000 !important;
        color: #fff !important;
        border-radius: 0px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("OMNI QUIZ")

api_key = st.secrets.get("GEMINI_API_KEY")
uploaded_file = st.file_uploader("Upload Document or Image", type=["txt", "pdf", "jpg", "png"])
manual_text = st.text_area("Or input text directly", height=150)

if st.button("Generate Assessment"):
    if not api_key:
        st.error("API Key missing.")
    elif not uploaded_file and not manual_text:
        st.warning("Please provide content.")
    else:
        with st.spinner("Refining..."):
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('models/gemini-3.5-flash')
                # (Keep your processing logic here)
                response = model.generate_content("Create a 5-question quiz.")
                
                st.markdown("---")
                # Forces output to be black
                st.markdown(f'<div style="color: #111111;">{response.text}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)
