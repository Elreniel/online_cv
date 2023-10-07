import streamlit as st
from streamlit_lottie import st_lottie
from animations.load_animations import load_lottiefile, load_lottieurl

def education():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("2021 - Present, Middle East Techical University")
        st.write("Ph.D. in Graduate School of Informatics, Information Systems/Data Science")

        st.subheader("2018 - 2021, Hacettepe University")
        st.write("M.Sc. in Computer Engineering")
        st.write("Thesis: Estimating Instrumentation Data Acquired During Flight Test of a Helicopter Using Predictor Models")

        st.subheader("2012 - 2017, Bilkent University")
        st.write("B.S. Electrical and Electronics Engineering")
        st.write("Senior Project: Detecting and Tracking Cars from DJI Phantom 3 Drone via NVDIA Jetson TX-1")

    with col2:
        education_animation = load_lottiefile("./animations/education.json")
        st_lottie(
            education_animation,
            speed=1,
            reverse=False,
            loop=True,
            quality="High"
        )
