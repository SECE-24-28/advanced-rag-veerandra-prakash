import os
import tempfile

import streamlit as st

from dotenv import load_dotenv

from src.pdf_loader import load_pdf
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.rag_chain import build_chain

load_dotenv()

st.set_page_config(
    page_title="Research Paper RAG Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Research Paper RAG Assistant")

uploaded_files = st.file_uploader(
    "Upload Research Papers",
    type="pdf",
    accept_multiple_files=True
)

if st.button("Process Papers"):

    all_docs = []

    with st.spinner("Processing Research Papers..."):

        for file in uploaded_files:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            ) as tmp_file:

                tmp_file.write(file.read())

                docs = load_pdf(tmp_file.name)

                all_docs.extend(docs)

        chunks = split_documents(all_docs)

        vector_db = create_vector_store(chunks)

        st.session_state["vector_db"] = vector_db

    st.success("Research Papers Indexed Successfully!")

st.divider()

question = st.text_input(
    "Ask a question about your research papers"
)

if question:

    if "vector_db" not in st.session_state:

        st.warning("Upload and process papers first.")

    else:

        chain = build_chain(
            st.session_state["vector_db"]
        )

        with st.spinner("Searching Papers..."):

            response = chain.run(question)

        st.subheader("Answer")

        st.write(response)