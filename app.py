import streamlit as st
import google.generativeai as genai
from PIL import Image
import PyPDF2
import base64

# --- Page Config ---
st.set_page_config(page_title="OmniQuiz | Bespoke", layout="wide")

# --- Luxury Glassmorphism & Background Video ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Ensure background.mp4 is in your GitHub repo
try:
    video_base64 = get_base64_of_bin_file('background.mp4')
    bg_style = f"""
    <style>
    .stApp {{
        background: url(data:video/mp4;base64,{video_base64});
        background-size: cover;
    }}
    .main-container {{
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(15px);
        padding: 40px;
        border: 1px solid rgba(255, 255, 255, 0.5);
        max-width: 800px;
        margin: auto;
    }}
    h1 {{ font-family: 'Helvetica', sans-serif; text-transform: uppercase; letter-spacing: 5px; color: #000; text-align: center; }}
    .stButton>button {{
        width: 100%; background: #000 !important; color: #fff !important;
        border: none !important; padding: 15px !important;
        letter-spacing: 3px !important; text-transform: uppercase !important;
        border-radius: 0px !important;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)
except:
    st.warning("Background video not found. Ensure 'background.mp4' is in your repository.")

# --- App Content ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("OMNI QUIZ")
st.markdown("<p style='text-align:center;'>ENGINEERED FOR PRECISION</p>", unsafe_allow_html=True)

api_key = st.secrets.get("GEMINI_API_KEY")
uploaded_file = st.file_uploader("Upload Document, Image, or Video", type=["txt", "pdf", "jpg", "png", "mp4"])
manual_text = st.text_area("Or input text directly", height=150)

if st.button("Generate Assessment"):
    if not api_key:
        st.error("API Key missing in Secrets.")
    elif not uploaded_file and not manual_text:
        st.warning("Please provide input.")
    else:
        with st.spinner("Processing..."):
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('models/gemini-3.5-flash')
                
                content = [manual_text] if manual_text else []
                if uploaded_file:
                    if uploaded_file.type.startswith("image"):
                        content.append(Image.open(uploaded_file))
                    elif uploaded_file.type == "application/pdf":
                        reader = PyPDF2.PdfReader(uploaded_file)
                        content.append("".join([p.extract_text() for p in reader.pages]))
                    else:
                        content.append("File uploaded.")

                response = model.generate_content(content + ["Create a 5-question multiple choice quiz."])
                st.markdown("---")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)
