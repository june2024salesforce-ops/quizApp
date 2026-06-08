import streamlit as st

st.set_page_config(page_title="Omni Quiz", layout="wide")

# 1. Background Video (YouTube direct)
# Hum isse ek dummy container mein daal rahe hain
st.markdown("""
    <style>
    /* Ye CSS video ko background mein dhakel degi */
    .stVideo {
        position: fixed;
        right: 0; bottom: 0;
        min-width: 100%; min-height: 100%;
        z-index: -1;
    }
    .content-box {
        background: rgba(255, 255, 255, 0.9);
        padding: 40px; border-radius: 20px;
        max-width: 600px; margin: 100px auto;
        color: #000; text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Video load karo (Muted + Autoplay)
st.video("https://www.youtube.com/watch?v=8KY6ZE44scQ", autoplay=True, loop=True, muted=True)

# 2. UI Content (Jo video ke upar dikhega)
st.markdown('<div class="content-box">', unsafe_allow_html=True)
st.title("OMNI QUIZ")
st.subheader("ENGINEERED FOR PRECISION")

uploaded_file = st.file_uploader("Upload content")
if st.button("GENERATE QUIZ"):
    st.write("Processing...")
st.markdown('</div>', unsafe_allow_html=True)
