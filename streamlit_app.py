import streamlit as st

st.set_page_config(page_title="Tsum Clause Profiler", layout="wide")

st.title("🧠 Tsum Clause Profiler")
st.markdown("Analyze and diagnose clause-level structure, risk, and drift.")

uploaded_file = st.file_uploader("Upload a document (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write("🚧 Clause parsing and profiling coming soon.")
else:
    st.info("Awaiting document upload...")

