import streamlit as st

st.set_page_config(page_title="Omni Quiz", layout="wide")

st.markdown("""
    <style>
    /* 1. Video Overlay (Controls) ko hide karna */
    .video-background {
        position: fixed; top: 0; left: 0;
        width: 100vw; height: 100vh;
        z-index: -1000; overflow: hidden;
    }
    .video-background iframe {
        width: 100vw; height: 100vh;
        pointer-events: none; /* Mouse disable */
    }

    /* 2. Streamlit ke default 'Upload' box aur baki containers ko hide karna */
    [data-testid="stFileUploader"] {
        background: rgba(0,0,0,0.3) !important;
        border: none !important;
    }
    
    /* WO BLACK BOX HATANE KE LIYE */
    section[data-testid="stSidebar"] { display: none; }
    [data-testid="stVerticalBlock"] > div:has(iframe) { display: none !important; }
    
    /* 3. Main UI Box */
    .main-box {
        background: rgba(0, 0, 0, 0.5) !important;
        padding: 40px; border-radius: 20px;
        max-width: 600px; margin: 150px auto;
        color: white !important; text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(5px);
    }
    </style>
    """, unsafe_allow_html=True)

# YouTube Video Embed
st.markdown("""
    <div class="video-background">
        <iframe src="https://www.youtube.com/embed/8KY6ZE44scQ?autoplay=1&mute=1&loop=1&playlist=8KY6ZE44scQ&controls=0&showinfo=0&modestbranding=1&playsinline=1&disablekb=1" 
        frameborder="0" allow="autoplay; encrypted-media"></iframe>
    </div>
    """, unsafe_allow_html=True)

# UI Box
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("OMNI QUIZ")
st.subheader("ENGINEERED FOR PRECISION")

# File Uploader
uploaded_file = st.file_uploader("Upload content")
if st.button("GENERATE QUIZ"):
    st.write("Processing...")
st.markdown('</div>', unsafe_allow_html=True)
