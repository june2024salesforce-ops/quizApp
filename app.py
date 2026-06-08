import streamlit as st
import google.generativeai as genai

# Page setup
st.set_page_config(page_title="QuizMaster AI", layout="centered")
st.title("🎓 AI Quiz Generator")

# Securely retrieve API Key from Streamlit Secrets
# (Make sure to save GEMINI_API_KEY in the Cloud 'Secrets' settings)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("API Key not found in Secrets. Please add GEMINI_API_KEY to your Streamlit Cloud settings.")
    st.stop()

# User Interface
doc_text = st.text_area("Paste your document text here (min 50 characters):", height=200)

if st.button("Generate Quiz", type="primary"):
    if doc_text and len(doc_text) > 50:
        with st.spinner("Generating your quiz..."):
            try:
                genai.configure(api_key=api_key)
                
                # Using the authorized Gemini 3.5 Flash model
                model = genai.GenerativeModel('gemini-3.5-flash')
                
                prompt = (f"Create a 5-question multiple choice quiz from this text. "
                          f"Include the answer key at the end. Text: {doc_text}")
                
                response = model.generate_content(prompt)
                
                st.markdown("---")
                st.markdown("### 📝 Your Quiz:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Generation Error: {e}")
    else:
        st.warning("Please paste at least 50 characters of text to generate a high-quality quiz.")
