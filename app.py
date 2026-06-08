import streamlit as st
import google.generativeai as genai
from PIL import Image
import PyPDF2
import os

# --- Page Config ---
st.set_page_config(page_title="OmniQuiz | Professional", layout="wide")

# --- Luxury Styling ---
st.markdown("""
    <style>
    .stApp { background: #FFFFFF !important; }
    .main-container { padding: 40px; max-width: 800px; margin: auto; color: #111111 !important; }
    h1 { color: #111111 !important; text-transform: uppercase; letter-spacing: 5px; text-align: center; }
    .stButton>button { background: #000 !important; color: #fff !important; border-radius: 0px !important; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("OMNI QUIZ")

api_key = st.secrets.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# --- Inputs ---
uploaded_file = st.file_uploader("Upload Document, Image, or Video", type=["txt", "pdf", "jpg", "png", "mp4"])

if uploaded_file:
    if uploaded_file.type == "video/mp4":
        st.video(uploaded_file) # Video UI mein dikhega

if st.button("Generate Assessment"):
    with st.spinner("Analyzing..."):
        try:
            model = genai.GenerativeModel('models/gemini-3.5-flash')
            
            # --- Video Processing Logic ---
            if uploaded_file and uploaded_file.type == "video/mp4":
                # Video ko upload karke processing (Gemini File API)
                video_file = genai.upload_file(uploaded_file)
                prompt = "Watch this video and create a 5-question multiple choice quiz. Put each option on a new line."
                response = model.generate_content([prompt, video_file])
            
            # --- Text/PDF Logic ---
            elif uploaded_file and uploaded_file.type == "application/pdf":
                reader = PyPDF2.PdfReader(uploaded_file)
                text = "".join([p.extract_text() for p in reader.pages])
                prompt = f"Create 5 questions from this text. Options must be on separate lines.\n\n{text}"
                response = model.generate_content(prompt)
                
            else:
                response = model.generate_content("Create a 5-question quiz.")

            st.markdown("---")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)
