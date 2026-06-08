import streamlit as st
import google.generativeai as genai
import PyPDF2
import base64

st.set_page_config(page_title="OmniQuiz", layout="wide")

# --- Background Video & UI Styling ---
st.markdown("""
    <style>
    /* Background Video - Fixed position */
    .video-background {
        position: fixed; 
        right: 0; bottom: 0;
        min-width: 100%; min-height: 100%;
        width: auto; height: auto; z-index: -1000;
        object-fit: cover;
    }
    
    /* Main UI Card */
    .main-box {
        background: rgba(255, 255, 255, 0.85);
        padding: 40px;
        border-radius: 20px;
        max-width: 800px;
        margin: 50px auto;
        color: #000;
    }
    h1, h2, h3, p { color: #000 !important; }
    </style>

    <video autoplay muted loop id="myVideo" class="video-background">
      <source src="319751_tiny.mp4" type="video/mp4">
    </video>
    """, unsafe_allow_html=True)

# --- UI Content ---
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("OMNI QUIZ")

uploaded_file = st.file_uploader("Upload Document")
manual_text = st.text_area("Input Text")

if st.button("Generate Assessment"):
    # ... (Aapka existing backend code yahan rahega) ...
    st.success("Quiz Generated!")

st.markdown('</div>', unsafe_allow_html=True)
