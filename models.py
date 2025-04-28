import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["google_api_key"])

@st.cache_resource
def get_model():
    model = genai.GenerativeModel('gemini-2.0-flash')

    def call_gemini(prompt):
        response = model.generate_content(prompt)
        return response.text  # Palautetaan pelkkä generoidun sisällön teksti

    return call_gemini
