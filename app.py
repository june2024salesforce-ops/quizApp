import streamlit as st
import google.generativeai as genai
from PIL import Image
import PyPDF2

# --- Page Config ---
st.set_page_config(page_title="OmniQuiz | Bespoke", layout="wide")

# --- UI Styling ---
st.markdown("""
    <style>
    .stApp { background: #FFFFFF !important; }
    .main-container { padding: 40px; max-width: 800px; margin: auto; }
    h1 { color: #000 !important; text-transform: uppercase; letter-spacing: 5px; text-align: center; }
    .stButton>button { background: #000 !important; color: #fff !important; width: 100%; border-radius: 0px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- Layout ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("OMNI QUIZ")

# Video Section (File root folder mein honi chahiye)
if st.checkbox("Show Background Video"):
    try:
        st.video("319751_tiny.mp4")
    except Exception as e:
        st.error("Video file nahi mili. Check karo file root folder mein hai ya nahi.")

# Content Input
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
                
                content_text = manual_text
                if uploaded_file and uploaded_file.type == "application/pdf":
                    reader = PyPDF2.PdfReader(uploaded_file)
                    content_text += "\n" + "".join([p.extract_text() for p in reader.pages])
                
                prompt = f"Create a 5-question multiple choice quiz. Provide options clearly. Keep each option on a new line.\n\nContent: {content_text}"
                response = model.generate_content(prompt)
                
                st.markdown("---")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)
