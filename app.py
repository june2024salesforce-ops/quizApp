import streamlit as st

st.set_page_config(page_title="Omni Quiz", layout="wide")

# CSS: Background, UI Box, aur "Ghost Box" hatane ke liye
st.markdown("""
    <style>
    /* 1. Reset all Streamlit containers */
    [data-testid="stAppViewContainer"], [data-testid="stApp"], [data-testid="stMainBlockContainer"] {
        background: transparent !important;
    }
    
    /* 2. Ye line us Green/Orange Box ko hide karegi */
    [data-testid="stMarkdownContainer"] {
        display: block !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* 3. Video Background */
    .video-background {
        position: fixed; top: 0; left: 0;
        width: 100vw; height: 100vh;
        z-index: -1000; overflow: hidden;
    }
    .video-background iframe {
        width: 100vw; height: 100vh;
        pointer-events: none;
    }
    
    /* 4. Floating UI Box */
    .main-box {
        background: rgba(0, 0, 0, 0.6) !important;
        padding: 40px; border-radius: 20px;
        max-width: 600px; margin: 150px auto;
        color: white !important; text-align: center;
        border: 1px solid rgba(255,255,255,0.2);
    }
    h1, h2, h3, p { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# YouTube Video Embed
st.markdown("""
    <div class="video-background">
        <iframe src="https://www.youtube.com/embed/8KY6ZE44scQ?autoplay=1&mute=1&loop=1&playlist=8KY6ZE44scQ&controls=0&showinfo=0&modestbranding=1&playsinline=1&disablekb=1" 
        frameborder="0" allow="autoplay; encrypted-media"></iframe>
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
