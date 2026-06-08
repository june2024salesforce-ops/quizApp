import streamlit as st

st.set_page_config(page_title="Omni Quiz", layout="wide")

# YouTube Background Video Logic
video_id = "8KY6ZE44scQ" 

st.markdown(f"""
    <style>
    /* Fullscreen background video */
    .video-background {{
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        z-index: -1;
        overflow: hidden;
    }}
    .video-background iframe {{
        width: 100vw; height: 100vh;
        pointer-events: none; /* User video ko click na kar sake */
    }}
    /* Luxury Floating UI */
    .main-box {{
        background: rgba(255, 255, 255, 0.9);
        padding: 50px; border-radius: 20px;
        max-width: 700px; margin: 100px auto;
        color: #000; text-align: center;
    }}
    </style>

    <div class="video-background">
        <iframe src="https://www.youtube.com/embed/{video_id}?autoplay=1&mute=1&loop=1&playlist={video_id}&controls=0&showinfo=0&modestbranding=1&playsinline=1" 
        frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)

# UI Elements (Floating)
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("OMNI QUIZ")
st.subheader("ENGINEERED FOR PRECISION")

uploaded_file = st.file_uploader("Upload content")
if st.button("GENERATE QUIZ"):
    st.write("Processing...")
st.markdown('</div>', unsafe_allow_html=True)
