import streamlit as st
import google.generativeai as genai
from PIL import Image
import PyPDF2
import os

# --- Page Config ---
st.set_page_config(page_title="OmniQuiz | Bespoke", layout="wide")

# --- Luxury UI + Background Video Logic ---
st.markdown("""
    <style>
    /* Background Video Styling */
    .video-container {
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%;
        min-height: 100%;
        z-index: -1;
    }
    
    /* Luxury Card Styling */
    .main-container {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(15px);
        padding: 50px;
        margin-top: 100px;
        border-radius: 0px;
        color: #000000 !important;
    }
    
    h1, p, label { color: #000000 !important; }
    .stButton>button { background: #000 !important; color: #fff !important; width: 100%; border-radius: 0px !important; }
    </style>
    """, unsafe_allow_html=True)

# Video Background Embed
video_file = "319751_tiny.mp4"
if os.path.exists(video_file):
    st.markdown(f'''
        <video class="video-container" autoplay loop muted playsinline>
            <source src="{video_file}" type="video/mp4">
        </video>
    ''', unsafe_allow_html=True)

# UI Layout
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("OMNI QUIZ")

uploaded_file = st.file_uploader("Upload Document or Image", type=["txt", "pdf", "jpg", "png"])
manual_text = st.text_area("Or input text directly", height=150)

if st.button("Generate Assessment"):
    if not uploaded_file and not manual_text:
        st.warning("Pehle content provide karo!")
    else:
        with st.spinner("Analyzing..."):
            try:
                genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
                model = genai.GenerativeModel('models/gemini-3.5-flash')
                
                content = manual_text
                if uploaded_file and uploaded_file.type == "application/pdf":
                    reader = PyPDF2.PdfReader(uploaded_file)
                    content += "\n" + "".join([p.extract_text() for p in reader.pages])
                
                response = model.generate_content(f"Create a 5-question quiz. Keep options on new lines.\n\nContent: {content}")
                st.markdown("---")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)
