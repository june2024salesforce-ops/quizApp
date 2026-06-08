import streamlit as st

st.set_page_config(page_title="Omni Quiz", layout="wide")

# Container setup for video
# Hum yahan 'autoplay' ke liye nahi, balki 'st.video' ka use karenge
st.markdown("""
    <style>
    .main-box {
        background: rgba(255, 255, 255, 0.9);
        padding: 40px; border-radius: 20px;
        max-width: 600px; margin: 100px auto;
        color: #000; text-align: center;
        z-index: 10; position: relative;
    }
    </style>
    """, unsafe_allow_html=True)

# Video Background (Directly using Streamlit's stable component)
# YouTube link ko st.video() ke andar daal do, autoplay=True ke saath
st.video("https://www.youtube.com/watch?v=8KY6ZE44scQ", autoplay=True, loop=True, muted=True, start_time=0)

# UI Elements
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("OMNI QUIZ")
st.subheader("ENGINEERED FOR PRECISION")
uploaded_file = st.file_uploader("Upload content")
if st.button("GENERATE QUIZ"):
    st.write("Processing...")
st.markdown('</div>', unsafe_allow_html=True)
