import streamlit as st
from streamlit_lottie import st_lottie
from animations.load_animations import load_lottiefile, load_lottieurl

def work_experience():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("October 2022 - Present, Data Scientist - ETIYA")
        st.write("Data Scientist in Akbank Mobile AI Team")
        st.write("Developed computer vision model to detect IBAN text via mobile phone camera")
        st.write("Developed LLM based (GPT3.5, Llama (version 1 and 2), Falcon) chatbot for both customers and employees")
        st.write("Finetuned different LLM for specific tasks and use embedding to search information from any document via LLM")

        st.subheader("August 2021 - October 2022 Data Scientist, orientis.ai")
        st.write("Developed computer vision based solutions for industry needs, especially for automobile industry")
        st.write("Developed Quality Assurance Box (QAB) for detecting any defect on handbrake")
        st.write("Integrated to production line in the factory, can communicate with other softwares such as SAP")

        st.subheader("August 2021 - October 2022 Data Scientist, Algomedicus")
        st.write("Developed computer vision based solutions for medical treatment")
        st.write("Deep Learning model to detect 13 different diseases from X-Ray image")
        st.write("Collaborated research with Hacettepe University")

        st.subheader("April 2018 - August 2021 Flight Test Instrumentation Engineer, Turkish Aerospace")
        st.write("Responsible for instrumentation on T129 ATAK Helicopter (Phase 1 and 2), T625 GÖKBEY Helicopter and T70 Utility Helicopter")
        st.write("Design and install data acquisition systems for 1000 sensors with different kinds and digital busses")
        st.write("Process the raw binary data into engineering values")
        st.write("Store and distribute data to other engineering departments")

        st.subheader("June 2015 - June 2016 Undergrad Researcher, Bilkent University")
        st.write("Developed machine learning algorithm for bioinformatic applications at Asst. Prof. Ercüment Çiçek's Research Group")
        st.write("Published an academic paper in IEEE/ACM Transactions on Computational Biology and Bioinformatics")



    with col2:
        work_experience_animation = load_lottiefile("./animations/work.json")
        st_lottie(
            work_experience_animation,
            speed=1,
            reverse=False,
            loop=True,
            quality="High"
        )