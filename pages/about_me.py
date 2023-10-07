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

        st.subheader("Publication")
        st.write("2021, Estimating Instrumentation Data Acquired During Flight Test of a Helicopter Using Predictor Models, IEEE EUROCON")
        st.write("2019, Predicting Carbon Spectrum in Heteronuclear Single Quantum Coherence Spectroscopy for Online Feedback During Surgey, IEEE/ACM Transactions on Computational Biology and Bioinformatics")

        st.subheader("Programming Skills")
        st.write("Python\tMatLab\tR\tSQL")

        st.subheader("Frameworks")
        st.write("Numpy\tPandas\tR\tScikit-Learn")
        st.write("Tensorflow-Keras\tPytorch\tHuggingface\tDetectron2")

    with col2:
        about_me_animation = load_lottiefile("./animations/about_me.json")
        st_lottie(
            about_me_animation,
            speed=1,
            reverse=False,
            loop=True,
            quality="High"
        )