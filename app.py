import streamlit as st

st.set_page_config(page_title="Omni Quiz", layout="wide")

# FINAL CSS FIX: Layering conflict solve karne ke liye
st.markdown("""
    <style>
    /* 1. Background layer transparent karo */
    [data-testid="stAppViewContainer"] {
        background: transparent !important;
    }
    [data-testid="stApp"] {
        background: transparent !important;
    }
    
    /* 2. Video ko fixed background banao */
    .video-background {
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        z-index: -10;
        object-fit: cover;
    }
    
    /* 3. Floating Content Box */
    .main-box {
        background: rgba(0, 0, 0, 0.6) !important;
        padding: 50px;
        border-radius: 20px;
        max-width: 600px;
        margin: 150px auto;
        color: white !important;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.2);
    }
    h1, h2, h3, p { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 4. Video Injection (Directly in main container)
st.markdown("""
    <video autoplay loop muted playsinline class="video-background">
      <source src="https://www.w3schools.com/howto/rain.mp4" type="video/mp4">
    </video>
    """, unsafe_allow_html=True)

# 5. UI Layout
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("OMNI QUIZ")
st.subheader("ENGINEERED FOR PRECISION")

uploaded_file = st.file_uploader("Upload content")
if st.button("GENERATE QUIZ"):
    st.write("Processing...")
st.markdown('</div>', unsafe_allow_html=True)
