import requests
import streamlit as st


def query(payload):
	API_URL = st.session_state['API']
	headers = {"Authorization": f"Bearer {st.secrets['HUGGINGFACE_TOKEN']}"}
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


def text_generation():
	if 'prompt' not in st.session_state:
		st.session_state['prompt'] = st.secrets['GPT2_ENDPOINT']
	if 'API' not in st.session_state:
		st.session_state['API'] = ''
	if 'continue' not in st.session_state:
		st.session_state['continue'] = False

	selected_llm = st.selectbox('Please select a LLM?', ('GPT-2', 'Falcon-7B-Instruct'))
	if selected_llm == 'GPT-2':
		st.session_state['API'] = st.secrets['GPT2_ENDPOINT']
	elif selected_llm == 'Falcon-7B-Instruct':
		st.session_state['API'] = st.secrets['FALCON7B_ENDPOINT']

	prompt = st.text_input("Enter a prompt, LLM will going to complete", "")
	if st.session_state['continue']:
		with st.spinner('Wait for it...'):
			st.session_state['prompt'] = query({"inputs": st.session_state['prompt']})[0]["generated_text"]
		st.write(st.session_state['prompt'])
	elif prompt:
		st.session_state['continue'] = False
		st.session_state['prompt'] = prompt
		with st.spinner('Wait for it...'):
			st.session_state['prompt'] = query({"inputs": st.session_state['prompt']})[0]["generated_text"]
		st.write(st.session_state['prompt'])


	st.session_state['continue'] = st.button("Continue?")
