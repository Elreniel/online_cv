import requests
import streamlit as st
import io
from PIL import Image

API_URL = st.secrets['STABLE_DIFFUSION_ENDPOINT']
headers = {"Authorization": f"Bearer {st.secrets['HUGGINGFACE_TOKEN']}"}


def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content


def stable_diffusion():
	prompt = st.text_input("Enter a prompt to generate a picture")
	if prompt:
		with st.spinner('Wait for it...'):
			image_bytes = query({"inputs": prompt})
			generated_image = Image.open(io.BytesIO(image_bytes))
		st.image(generated_image, caption=prompt, use_column_width="always")