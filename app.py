import streamlit as st

st.title("PII Redaction Tool")

uploaded_file = st.file_uploader("Upload a DOCX file", type=["docx"])

if uploaded_file:
    st.success("File uploaded successfully!")
    st.write("Connect this to your redaction functions in main.py.")