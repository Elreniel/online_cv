import streamlit as st
import requests

API_URL = st.secrets['QA_ENDPOINT']
CONTEXT = st.secrets['CONTEXT']
headers = {"Authorization": f"Bearer {st.secrets['HUGGINGFACE_TOKEN']}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def chatbot():
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if question := st.chat_input("Ask me a question about Barış Coşkun"):
        st.session_state["messages"].append({"role": "user", "content": question})

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Wait for it..."):
                message_placeholder = st.empty()
                full_response = ""
                assistant_response = query({"inputs":
                                                {"question": question,
                                                 "context": CONTEXT}})["answer"]
            for chunk in assistant_response.split():
                full_response += chunk + " "
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(f"{full_response}")
        st.session_state.messages.append({"role": "assistant", "content": full_response})