import streamlit as st
from pages.stable_diffusion import stable_diffusion
from pages.text_generation import text_generation
from pages.chatbot import chatbot
from pages.detection import detection


def projects():
    st.write("These are sample demonstrations of my professional projects. Due to the hardware requirements of models, I am using simple APIs instead. However, in my professional projects, I am using more complex models with custom implementations.")

    selected_project = st.selectbox(
        'Please select a project for demo?',
        ("Chatbot", 'Stable Diffusion', "Detection"))

    if selected_project == "Stable Diffusion":
        stable_diffusion()
    elif selected_project == "Text Completion":
        text_generation()
    elif selected_project == "Chatbot":
        chatbot()
    elif selected_project == "Detection":
        detection()
