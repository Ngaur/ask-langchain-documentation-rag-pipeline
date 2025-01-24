import os
import zipfile
import streamlit as st

default_session_state = {
    "ingested": False
}

def validation():
    pass


def initialize_state() -> None:
    for key,value in default_session_state.items():
        if key not in st.session_state:
            st.session_state[key] = value

# Function to extract files from the uploaded zip
def extract_zip(zip_file, extract_to="temp"):
    with zipfile.ZipFile(zip_file, "r") as zf:
        zf.extractall(extract_to)