import streamlit as st
from streamlit_lottie import st_lottie
from animations.load_animations import load_lottiefile, load_lottieurl


def about_me():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Background Info")
        st.write("Data Scientist especially interested in Computer Vision, Predictive Models and Optimization")
        st.write("Advance understanding of data analysis and processing")
        st.write("Highly motivated to design algorithms for real-life problems")
        st.write("Motocycle Enthusiast")

        st.subheader("Publication")
        st.write("[Estimating Instrumentation Data Acquired During Flight Test of a Helicopter Using Predictor Models](https://ieeexplore.ieee.org/document/9535625)")
        st.write("[Predicting Carbon Spectrum in Heteronuclear Single Quantum Coherence Spectroscopy for Online Feedback During Surgery](https://ieeexplore.ieee.org/abstract/document/8730423)")

        st.subheader("Programming Skills")
        col11, col12 = st.columns(2)
        with col11:
            st.write("Python")
            st.write("SQL")
            st.write("R ")
            st.write("MatLab")
        with col12:
            st.write("★ ★ ★ ★ ★")
            st.write("★ ★ ★ ☆ ☆")
            st.write("★ ★ ★ ☆ ☆")
            st.write("★ ★ ★ ☆ ☆")

        st.subheader("Frameworks")
        col11, col12 = st.columns(2)
        with col11:
            st.write("Numpy")
            st.write("Pandas")
            st.write("Scikit ")
            st.write("Tensorflow-Keras")
            st.write("Pytorch")
            st.write("Huggingface")
            st.write("Detectron 2")
        with col12:
            st.write("★ ★ ★ ★ ★")
            st.write("★ ★ ★ ★ ★")
            st.write("★ ★ ★ ★ ★")
            st.write("★ ★ ★ ★ ☆")
            st.write("★ ★ ★ ★ ☆")
            st.write("★ ★ ★ ☆ ☆")
            st.write("★ ★ ★ ☆ ☆")

    with col2:
        about_me_animation = load_lottiefile("./animations/about_me.json")
        st_lottie(
            about_me_animation,
            speed=1,
            reverse=False,
            loop=True,
            quality="High"
        )