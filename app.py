import streamlit as st
import google.generativeai as genai
from PIL import Image
import PyPDF2
import os

# --- Page Config ---
st.set_page_config(page_title="OmniQuiz | Bespoke", layout="wide")

# --- UI Styling (High Visibility & Luxury) ---
st.markdown("""
    <style>
    /* White background force */
    .stApp { background-color: #FFFFFF !important; }
    
    /* Luxury Container */
    .main-container {
        padding: 40px;
        max-width: 800px;
        margin: auto;
        color: #000000 !important;
    }
    
    /* Text Visibility Force */
    h1, h2, h3, p, div, label, span { color: #000000 !important; }
    
    /* Buttons */
    .stButton>button {
        background-color: #000000 !important;
        color: #FFFFFF !important;
        border-radius: 0px !important;
        border: none !important;
        width: 100%;
        padding: 15px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- App Layout ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("OMNI QUIZ")

# Video Player Section
if st.checkbox("Show Background Video"):
    if os.path.exists("319751_tiny.mp4"):
        st.video("319751_tiny.mp4")
    else:
        st.error("Video file '319751_tiny.mp4' repository mein nahi mili. Check karo file root folder mein hai.")

# Content Input
uploaded_file = st.file_uploader("Upload Document or Image", type=["txt", "pdf", "jpg", "png"])
manual_text = st.text_area("Or input text directly", height=150)

if st.button("Generate Assessment"):
    if not uploaded_file and not manual_text:
        st.warning("Pehle content provide karo!")
    else:
        with st.spinner("Analyzing content..."):
            try:
                genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
                model = genai.GenerativeModel('models/gemini-3.5-flash')
                
                # Content processing
                content_text = manual_text if manual_text else ""
                if uploaded_file and uploaded_file.type == "application/pdf":
                    reader = PyPDF2.PdfReader(uploaded_file)
                    content_text += "\n" + "".join([p.extract_text() for p in reader.pages])
                elif uploaded_file:
                    content_text += "\n" + "User uploaded a file."
                
                # Generation
                prompt = f"Create a 5-question quiz. Provide options clearly. Keep each option on a new line.\n\nContent: {content_text}"
                response = model.generate_content(prompt)
                
                st.markdown("---")
                st.markdown(f"<div style='color: #000000; font-size: 18px;'>{response.text.replace(chr(10), '<br>')}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)
