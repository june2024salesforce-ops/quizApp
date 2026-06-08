import streamlit as st

st.set_page_config(page_title="Omni Quiz", layout="wide")

# CSS: Video ko background mein 'lock' karne ke liye
st.markdown("""
    <style>
    /* 1. Video Background Setup */
    .video-background {
        position: fixed;
        right: 0; bottom: 0;
        min-width: 100%; min-height: 100%;
        width: auto; height: auto;
        z-index: -100; /* Isse video sabse peeche rahegi */
        object-fit: cover;
    }
    
    /* 2. UI Floating Box */
    .main-box {
        background: rgba(0, 0, 0, 0.6); /* Transparent Dark Box */
        padding: 40px;
        border-radius: 20px;
        max-width: 600px;
        margin: 100px auto;
        color: white;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Text Color Fix */
    h1, h2, h3, p, label { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# Video Background (HTML5 tag)
# Yahan apni video ka URL daalo
st.markdown("""
    <video autoplay loop muted playsinline class="video-background">
      <source src="https://www.w3schools.com/howto/rain.mp4" type="video/mp4">
    </video>
    """, unsafe_allow_html=True)

# UI Elements (Box ke andar)
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("OMNI QUIZ")
st.subheader("ENGINEERED FOR PRECISION")

uploaded_file = st.file_uploader("Upload content")
if st.button("GENERATE QUIZ"):
    st.write("Processing...")
st.markdown('</div>', unsafe_allow_html=True)
