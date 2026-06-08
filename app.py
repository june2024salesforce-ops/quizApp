import streamlit as st
import google.generativeai as genai
from PIL import Image
import PyPDF2

# --- Page Config ---
st.set_page_config(page_title="OmniQuiz | Bespoke", layout="wide")

# --- Luxury Styling ---
st.markdown("""
    <style>
    .stApp { background: #FFFFFF !important; }
    .main-container { padding: 40px; max-width: 800px; margin: auto; color: #111111 !important; }
    h1 { color: #111111 !important; text-transform: uppercase; letter-spacing: 5px; text-align: center; }
    .stButton>button { background: #000 !important; color: #fff !important; border-radius: 0px !important; width: 100%; }
    .quiz-output { color: #111111 !important; font-size: 18px !important; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("OMNI QUIZ")

# Video Section (Ab yahan sahi file name use ho raha hai)
if st.checkbox("Show Background Video"):
    try:
        st.video("319751_tiny.mp4")
    except:
        st.error("Video file '319751_tiny.mp4' repository mein nahi mili. Check karo ki upload sahi se hua hai ya nahi.")

# File Uploader
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
                
                # Content processing logic
                content = manual_text
                if uploaded_file and uploaded_file.type == "application/pdf":
                    reader = PyPDF2.PdfReader(uploaded_file)
                    content += "\n" + "".join([p.extract_text() for p in reader.pages])
                
                # Prompting for clean output
                prompt = f"Create a 5-question multiple choice quiz. Provide options clearly. Keep a newline between each question and option.\n\nContent: {content}"
                response = model.generate_content(prompt)
                
                st.markdown("---")
                # Visibility ke liye div use kiya hai
                st.markdown(f'<div class="quiz-output">{response.text.replace(chr(10), "<br>")}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)
