import streamlit as st

st.set_page_config(page_title="Omni Quiz", layout="wide")

st.markdown("""
    <style>
    /* 1. App background transparent */
    [data-testid="stAppViewContainer"] { background: transparent !important; }
    
    /* 2. Video Background (Fixed) */
    .video-background {
        position: fixed; top: 0; left: 0;
        width: 100vw; height: 100vh;
        z-index: -1000; overflow: hidden;
    }
    
    /* 3. YE CONTROLS KO GAYAB KARNE WALA ASLI CODE HAI */
    video {
        width: 100vw; height: 100vh;
        object-fit: cover;
        pointer-events: none; /* Mouse click bhi nahi hoga video pe */
    }
    
    /* 4. UI Floating Box */
    .main-box {
        background: rgba(0, 0, 0, 0.6) !important;
        padding: 40px; border-radius: 20px;
        max-width: 600px; margin: 150px auto;
        color: white !important; text-align: center;
        border: 1px solid rgba(255,255,255,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# Video (Note: Yahan 'controls' attribute nahi likha hai)
st.markdown("""
    <div class="video-background">
        <video autoplay loop muted playsinline>
            <source src="https://www.w3schools.com/howto/rain.mp4" type="video/mp4">
        </video>
    </div>
    """, unsafe_allow_html=True)

# UI Elements
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("OMNI QUIZ")
st.subheader("ENGINEERED FOR PRECISION")

uploaded_file = st.file_uploader("Upload content")
if st.button("GENERATE QUIZ"):
    st.write("Processing...")
st.markdown('</div>', unsafe_allow_html=True)
