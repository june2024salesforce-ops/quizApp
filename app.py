import streamlit as st
import google.generativeai as genai
from PIL import Image
import PyPDF2

# --- Page Configuration ---
st.set_page_config(page_title="OmniQuiz | Bespoke", layout="wide")

# --- Luxury Aesthetic Styling ---
st.markdown("""
    <style>
    /* Global Page Styling */
    .stApp { 
        background: linear-gradient(135deg, #ffffff 0%, #f4f4f4 100%) !important; 
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
    }
    .main-container {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(20px);
        padding: 50px;
        border: 1px solid rgba(0, 0, 0, 0.1);
        max-width: 800px;
        margin: auto;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }
    h1 { 
        text-transform: uppercase; 
        letter-spacing: 6px !important; 
        color: #000000 !important; 
        text-align: center; 
        font-weight: 200 !important;
    }
    .stButton>button {
        width: 100%; 
        background: #000000 !important; 
        color: #ffffff !important;
        border: none !important; 
        padding: 15px !important;
        letter-spacing: 3px !important; 
        text-transform: uppercase !important;
        border-radius: 0px !important;
        transition: 0.3s;
    }
    .stButton>button:hover { background: #333333 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- App Structure ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.title("OMNI QUIZ")
st.markdown("<p style='text-align:center; color: #666; letter-spacing: 2px;'>ENGINEERED FOR PRECISION</p>", unsafe_allow_html=True)

# --- Input Section ---
api_key = st.secrets.get("GEMINI_API_KEY")
uploaded_file = st.file_uploader("Upload Document or Image", type=["txt", "pdf", "jpg", "png"])
manual_text = st.text_area("Or input text directly", height=150)

# --- Processing Engine ---
if st.button("Generate Assessment"):
    if not api_key:
        st.error("API Key missing. Check Streamlit Secrets.")
    elif not uploaded_file and not manual_text:
        st.warning("Please provide input.")
    else:
        with st.spinner("Analyzing content..."):
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
                        content.append(uploaded_file.read().decode("utf-8", errors="ignore"))

                response = model.generate_content(content + ["Create a 5-question multiple choice quiz with an answer key."])
                
                st.markdown("---")
                st.write(response.text)
            except Exception as e:
                st.error(f"Generation Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)
