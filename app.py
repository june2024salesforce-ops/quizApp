import streamlit as st

st.set_page_config(page_title="Omni Quiz", layout="wide")

# CSS: Moving gradient background (Live wallpaper jaisa)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(-45deg, #000000, #1a1a1a, #000000, #333333);
        background-size: 400% 400%;
        animation: gradient 10s ease infinite;
    }
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .main-box {
        background: rgba(255, 255, 255, 0.05);
        padding: 40px; border-radius: 20px;
        max-width: 600px; margin: 100px auto;
        color: white; text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
    }
    h1, h2, h3, p { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# UI Elements
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("OMNI QUIZ")
st.subheader("ENGINEERED FOR PRECISION")

uploaded_file = st.file_uploader("Upload content")
if st.button("GENERATE QUIZ"):
    st.write("Processing...")
st.markdown('</div>', unsafe_allow_html=True)
