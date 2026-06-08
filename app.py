import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="QuizMaster AI", layout="centered")
st.title("🎓 AI Quiz Generator")

# Securely retrieve the key from Streamlit Secrets
# If the app is run locally, it looks in .streamlit/secrets.toml
# If deployed on Streamlit Cloud, it looks in the Cloud Dashboard Secrets
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("API Key not found! Please set it in Streamlit Cloud Secrets.")
    st.stop()

doc_text = st.text_area("Paste your document text here:", height=200)

if st.button("Generate Quiz", type="primary"):
    if doc_text and len(doc_text) > 50:
        with st.spinner("Generating your quiz..."):
            try:
                genai.configure(api_key=api_key)
               model = genai.GenerativeModel('gemini-1.5')
                prompt = f"Create a 5-question multiple choice quiz from this text: {doc_text}. Output it clearly."
                response = model.generate_content(prompt)
                st.markdown("---")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please paste at least 50 characters of text.")
