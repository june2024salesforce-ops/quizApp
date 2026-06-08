import streamlit as st
import base64
import os

st.set_page_config(page_title="Omni Quiz", layout="wide")

def get_video_base64(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            return base64.b64encode(data).decode()
    return None

video_b64 = get_video_base64("319751_tiny.mp4")

# --- UI + Background Video ---
st.markdown(f"""
    <style>
    .video-background {{
        position: fixed; right: 0; bottom: 0;
        min-width: 100%; min-height: 100%;
        width: auto; height: auto; z-index: -1;
        object-fit: cover;
    }}
    .main-box {{
        background: rgba(255, 255, 255, 0.9);
        padding: 50px; border-radius: 10px;
        max-width: 700px; margin: 100px auto;
        color: #000; text-align: center;
    }}
    </style>
    <video autoplay loop muted playsinline class="video-background">
        <source src="data:video/mp4;base64,{video_b64}" type="video/mp4">
    </video>
    <div class="main-box">
        <h1>OMNI QUIZ</h1>
        <p>ENGINEERED FOR PRECISION</p>
    </div>
    """, unsafe_allow_html=True)

# Streamlit controls (Card ke andar)
with st.container():
    st.markdown('<div style="max-width:700px; margin:auto; background:rgba(255,255,255,0.9); padding:20px;">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload content")
    if st.button("GENERATE QUIZ"):
        st.write("Generating...")
    st.markdown('</div>', unsafe_allow_html=True)
