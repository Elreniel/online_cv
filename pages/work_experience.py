import streamlit as st
from streamlit_lottie import st_lottie
from animations.load_animations import load_lottiefile, load_lottieurl

def work_experience():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("October 2022 - Present, Data Scientist - ETIYA")
        st.write("Data Scientist in Akbank Mobile AI Team")
        st.write("Developed computer vision model to detect IBAN text via mobile phone camera")
        st.write("Implemented LLM based (GPT-3.5, Llama (version 1 and 2), Falcon) chatbot for both customers and employees")
        st.write("Finetuned different LLM for specific tasks")
        st.write("Use word embedding to search information from any document via LLM")
        st.divider()

        st.subheader("August 2021 - October 2022 Data Scientist, orientis.ai")
        st.write("Developed computer vision based solutions for industry needs, especially for automobile industry")
        st.write("Designed Quality Assurance Box (QAB) for detecting any defect on handbrake in real time")
        st.write("End-to-end automated product with proper User Interface and Model Finetuning")
        st.write("Integrated to production line in the factory, can communicate with other software such as SAP")
        st.divider()

        st.subheader("August 2021 - October 2022 Data Scientist, Algomedicus")
        st.write("Developed computer vision based solutions for medical treatment")
        st.write("Deep Learning model to detect 13 different diseases from Human Lung X-Ray")
        st.write("Collaborated research with Hacettepe University")
        st.divider()

        st.subheader("April 2018 - August 2021 Flight Test Instrumentation Engineer, Turkish Aerospace")
        st.write("Responsible for instrumentation on T129 ATAK Helicopter (Phase 1 and 2), T625 GÖKBEY Helicopter and T70 Utility Helicopter")
        st.write("Design and install data acquisition systems for 1000 sensors with different kinds and digital busses")
        st.write("Process the raw binary data into engineering values")
        st.write("Store and distribute data to other engineering departments")
        st.divider()

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