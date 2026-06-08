import streamlit as st

# Page configuration
st.set_page_config(page_title="Omni Quiz", layout="wide")

# 1. Background Video (Built-in Streamlit component - Sabse reliable)
# YouTube link ko st.video mein direct daalo, ye khud handle karega
st.markdown(
    """
    <style>
    [data-testid="stVideo"] {
        position: fixed;
        right: 0; bottom: 0;
        min-width: 100%; min-height: 100%;
        width: auto; height: auto; z-index: -1;
        object-fit: cover;
    }
    .main-box {
        background: rgba(255, 255, 255, 0.9);
        padding: 40px; border-radius: 20px;
        max-width: 600px; margin: 100px auto;
        color: #000; text-align: center;
    }
    </style>
    """, unsafe_allow_html=True
)

# Background video play karo
st.video("https://www.youtube.com/watch?v=8KY6ZE44scQ", autoplay=True, loop=True, muted=True)

# 2. UI Content
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("OMNI QUIZ")
st.subheader("ENGINEERED FOR PRECISION")

uploaded_file = st.file_uploader("Upload content")
if st.button("GENERATE QUIZ"):
    st.write("Processing...")
st.markdown('</div>', unsafe_allow_html=True)
