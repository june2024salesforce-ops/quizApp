import streamlit as st
import google.generativeai as genai

st.title("Debug Tool")

# Put your key in the box on the website
api_key = st.text_input("Paste your API Key here", type="password")

if st.button("Find My Models"):
    if api_key:
        genai.configure(api_key=api_key)
        # This will list the exact names allowed for your specific key
        st.write("Looking for your models...")
        try:
            model_list = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            st.write("Use one of these names exactly as written:")
            st.write(model_list)
        except Exception as e:
            st.error(f"Error: {e}")
