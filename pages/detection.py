import requests
import streamlit as st
from PIL import Image, ImageDraw

API_URL = API_URL = st.secrets['DETECTION_ENDPOINT']
headers = {"Authorization": f"Bearer {st.secrets['HUGGINGFACE_TOKEN']}"}


def query(uploaded_file):
    response = requests.post(API_URL, headers=headers, data=uploaded_file)
    return response.json()


def detection():
    source_img = st.file_uploader("Upload Image")
    if source_img:
        with st.spinner('Wait for it...'):
            try:
                output = query(source_img)
                source_img = Image.open(source_img)
                for tempDetection in output:
                    draw = ImageDraw.Draw(source_img)
                    xmin, ymin, xmax, ymax = tempDetection["box"]["xmin"], tempDetection["box"]["ymin"], tempDetection["box"]["xmax"], tempDetection["box"]["ymax"]
                    draw.rectangle(((xmin, ymin), (xmax, ymax)), outline="black")
                    text = f"Class: {tempDetection['label']}, Score: {tempDetection['score']}"
                    draw.text((xmin, ymin), text, fill="black")
                st.image(source_img, use_column_width="always")
            except:
                st.write("Something went wrong with API. Please try again later.")
