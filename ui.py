import os
import streamlit as st

import helper
import constant as const
from ingestion import ingest
from RAG_main import retreive_and_augment


st.set_page_config(
    page_title="Documentation Assistant"
)

helper.initialize_state()

st.header(const.PAGE_HEADING, divider="rainbow")

st.info(const.INFO_MESSAGE)

ingestion, retreival = st.tabs(["Ingestion", "Retreival"])

with ingestion:
    if st.session_state.ingested:
        st.warning("document has already been ingested")
    else:   
        uploaded_zip = st.file_uploader(label="Upload ReadTheDoc documentation as zip file", 
                                type="zip",
                                disabled=st.session_state.ingested)
        if uploaded_zip:
            with st.status(const.INGESTION_STATUS_MESSAGE):
                st.write("1. uploading.....")
                os.makedirs(const.TEMP_DIRECTORY_NAME, exist_ok=True)
                zip_path = os.path.join(const.TEMP_DIRECTORY_NAME, uploaded_zip.name)
                with open(zip_path, "wb") as zip_file:
                    zip_file.write(uploaded_zip.read())
                st.write("2. extracting.....")
                helper.extract_zip(zip_path)
                st.write("ingestion to vector store")
                success_message = ingest(doc_path=os.path.splitext(zip_path)[0])
            
            st.session_state.ingested = True
            st.success(success_message)

with retreival:
    if not st.session_state.ingested:
        st.error("Document has not been ingested yet. Please do ingestion first")
    else:
        query = st.text_input(label='Ask your query on your ingested document')
        submit_btn = st.button("Submit query")
        if submit_btn:
            with st.spinner("Retreiving....."):
                results = retreive_and_augment(query)
            st.info(f"Human : {results['input']} \n\n AI : {results['answer']}")
            st.subheader("Supported Documents")
            st.info([f"{index}.{doc.metadata['source']}" for index, doc in enumerate(results['context'])])


