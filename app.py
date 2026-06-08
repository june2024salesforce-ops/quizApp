import streamlit as st
import google.generativeai as genai

st.title("API Debugger")

api_key = st.text_input("Enter API Key")
if st.button("List Available Models"):
    if api_key:
        genai.configure(api_key=api_key)
        # List all models and print their names
        models = [m.name for m in genai.list_models()]
        st.write("Available models for your key:")
        st.write(models)
    else:
        st.error("Please enter your key.")
