import streamlit as st
import google.generativeai as genai
from PIL import Image
import PyPDF2

# --- Page Config ---
st.set_page_config(page_title="OmniQuiz | Professional", layout="wide")

# --- Luxury Styling ---
st.markdown("""
    <style>
    .stApp { background: #FFFFFF !important; }
    .main-container {
        background: #FFFFFF;
        padding: 40px;
        max-width: 800px;
        margin: auto;
        color: #111111 !important;
    }
    h1, h2, h3, p, div, label { color: #111111 !important; }
    textarea { 
        background: #F4F4F4 !important; 
        color: #000000 !important; 
        border: 1px solid #333 !important; 
    }
    .stButton>button {
        background: #000 !important;
        color: #fff !important;
        border-radius: 0px !important;
        padding: 10px 20px;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- App Layout ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("OMNI QUIZ")
st.markdown("<p style='text-align:center;'>ENGINEERED FOR PRECISION</p>", unsafe_allow_html=True)

api_key = st.secrets.get("GEMINI_API_KEY")

# --- Inputs ---
uploaded_file = st.file_uploader("Upload your document (PDF, Image, Text)", type=["txt", "pdf", "jpg", "png"])
manual_text = st.text_area("Or input text directly", height=150)

# --- Processing Engine ---
if st.button("Generate Assessment"):
    if not api_key:
        st.error("API Key missing in Secrets.")
    elif not uploaded_file and not manual_text:
        st.warning("Please provide input content.")
    else:
        with st.spinner("Analyzing content..."):
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('models/gemini-3.5-flash')
                
                # Extracting content
                content_text = manual_text if manual_text else ""
                if uploaded_file:
                    if uploaded_file.type.startswith("image"):
                        img = Image.open(uploaded_file)
                        # For images, we pass the image object directly
                        response = model.generate_content(["Create a 5-question multiple choice quiz based on this image.", img])
                        st.markdown("---")
                        st.write(response.text)
                        st.stop()
                    elif uploaded_file.type == "application/pdf":
                        reader = PyPDF2.PdfReader(uploaded_file)
                        content_text += "\n" + "".join([p.extract_text() for p in reader.pages])
                    else:
                        content_text += "\n" + uploaded_file.read().decode("utf-8", errors="ignore")

                # Generating quiz from text
                prompt = f"""
                You are an expert quiz creator. Create a 5-question multiple choice quiz based ONLY on the text below. 
                Provide answers at the end. Do not add any conversational filler.
                
                CONTENT:
                {content_text}
                """
                response = model.generate_content(prompt)
                
                st.markdown("---")
                st.markdown(f'<div style="color: #111111; font-size: 16px;">{response.text}</div>', unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Generation Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)
