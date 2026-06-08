import streamlit as st

st.set_page_config(page_title="Omni Quiz", layout="wide")

# CSS aur JS injection (Force autoplay)
st.markdown("""
    <style>
    .video-container {
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        z-index: -1;
        object-fit: cover;
    }
    .main-box {
        background: rgba(255, 255, 255, 0.9);
        padding: 40px; border-radius: 20px;
        max-width: 600px; margin: 100px auto;
        color: #000; text-align: center;
    }
    </style>

    <video autoplay muted loop playsinline class="video-container" id="bgVideo">
        <source src="https://www.w3schools.com/howto/rain.mp4" type="video/mp4">
    </video>
    
    <script>
        var vid = document.getElementById("bgVideo");
        vid.muted = true;
        vid.play();
    </script>
    """, unsafe_allow_html=True)

# UI Elements
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("OMNI QUIZ")
uploaded_file = st.file_uploader("Upload content")
if st.button("GENERATE QUIZ"):
    st.write("Processing...")
st.markdown('</div>', unsafe_allow_html=True)
