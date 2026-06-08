import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Omni Quiz", layout="wide")

# --- UI + Background CSS ---
st.markdown("""
    <style>
    /* Force background white/dark and clean layout */
    .stApp {
        background-color: #000000;
        background-image: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    .main-box {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        padding: 50px;
        border-radius: 20px;
        max-width: 700px;
        margin: 100px auto;
        color: #FFFFFF;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    h1 { color: #FFFFFF !important; font-weight: 800; }
    .stButton>button { background: #FFFFFF !important; color: #000 !important; width: 100%; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- Layout ---
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("OMNI QUIZ")
st.subheader("ENGINEERED FOR PRECISION")

uploaded_file = st.file_uploader("Upload content")
if st.button("GENERATE QUIZ"):
    st.write("Processing...")
st.markdown('</div>', unsafe_allow_html=True)
