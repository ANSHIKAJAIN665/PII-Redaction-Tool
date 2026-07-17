import streamlit as st
import tempfile
import os

from main import redact_document

st.title("PII Redaction Tool")

uploaded_file = st.file_uploader(
    "Upload DOCX File",
    type=["docx"]
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp.write(uploaded_file.read())
        input_path = tmp.name

    output_path = "Redacted_Prospectus.docx"

    with st.spinner("Redacting document..."):
        redact_document(input_path, output_path)

    st.success("Redaction Completed!")

    with open(output_path, "rb") as f:
        st.download_button(
            "Download Redacted Document",
            data=f,
            file_name="Redacted_Prospectus.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )

    os.remove(input_path)