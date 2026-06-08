import streamlit as st
import google.generativeai as genai
from PIL import Image
import PyPDF2

# --- Page Configuration ---
st.set_page_config(page_title="OmniQuiz AI", page_icon="🎓", layout="wide")

# --- CSS Styling (Fixed) ---
st.markdown("""
    <style>
    /* Force background to white and text to black */
    .stApp {
        background-color: #FFFFFF !important;
    }
    h1, h2, h3, p, div, label {
        color: #1A1A1A !important;
    }
    textarea {
        background-color: #F8F9FA !important;
        color: #000000 !important;
        border: 1px solid #CCCCCC !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 OmniQuiz AI")
st.subheader("Drag and drop any file (Text, PDF, Image) to generate a quiz.")

# --- API Setup ---
api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("API Key not found in Secrets. Please add it to your Streamlit dashboard.")
    st.stop()

# --- Inputs ---
col1, col2 = st.columns([1, 1])
with col1:
    uploaded_file = st.file_uploader("Drop your file here", type=["txt", "pdf", "jpg", "png"])
with col2:
    manual_text = st.text_area("Or paste content directly:", height=150)

# --- Processing Logic ---
if st.button("Generate Premium Quiz", type="primary"):
    if not uploaded_file and not manual_text:
        st.warning("Please provide a file or text.")
    else:
        with st.spinner("OmniQuiz is analyzing your content..."):
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('models/gemini-3.5-flash')
                
                content_payload = [manual_text] if manual_text else []
                
                # Logic for file processing
                if uploaded_file:
                    if uploaded_file.type.startswith("image"):
                        content_payload.append(Image.open(uploaded_file))
                    elif uploaded_file.type == "application/pdf":
                        reader = PyPDF2.PdfReader(uploaded_file)
                        text = "".join([page.extract_text() for page in reader.pages])
                        content_payload.append(text)
                    elif uploaded_file.type == "text/plain":
                        content_payload.append(uploaded_file.read().decode("utf-8"))

                # Final Generation
                response = model.generate_content(content_payload + ["Create a 5-question multiple choice quiz with an answer key."])
                
                st.markdown("---")
                st.markdown("### 📝 Your Quiz:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Generation Error: {e}")
