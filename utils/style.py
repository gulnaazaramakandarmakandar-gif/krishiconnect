import streamlit as st

def apply_custom_css():

    st.markdown("""
    <style>

    .stApp {
        background-color: #f5fff5;
    }

    h1, h2, h3 {
        color: green;
    }

    div.stButton > button {
        background-color: #2e7d32;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px;
        font-weight: bold;
    }

    div.stButton > button:hover {
        background-color: #1b5e20;
        color: white;
    }

    </style>
    """, unsafe_allow_html=True)