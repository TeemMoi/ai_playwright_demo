import streamlit as st
from generate_test import generate_code

st.title("Playwright-testigeneraattori")
prompt = st.text_area("Anna testikuvaus suomeksi")
if st.button("Generoi testi"):
    code = generate_code(prompt)
    st.code(code, language='typescript')
