import streamlit as st
import requests

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chatbot")
st.write("Chat with your local AI using Ollama")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Type your message...")

if prompt:
    # Display user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Send message to Ollama
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "llama3.2",
                "messages": st.session_state.messages,
                "stream": False
            }
        )

        if response.status_code == 200:
            data = response.json()
            answer = data["message"]["content"]

            with st.chat_message("assistant"):
                st.markdown(answer)

            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

        else:
            st.error("Ollama returned an error. Make sure Ollama is running.")

    except Exception as e:
        st.error(
            "Could not connect to Ollama. Please make sure Ollama is running."
        )