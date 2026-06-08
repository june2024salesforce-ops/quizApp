import streamlit as st
import google.generativeai as genai

st.title("AI Quiz Generator")

# Get API Key from user
api_key = GEMINI_API_KEY = "YOUR_ACTUAL_API_KEY_HERE"
doc_text = st.text_area("Paste your document text here")

if st.button("Generate Quiz"):
    if api_key and doc_text:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Create a 5-question quiz from this text: {doc_text}. Provide questions and answers in a list."
        response = model.generate_content(prompt)
        st.write(response.text)
    else:
        st.error("Please enter your API Key and some text!")
