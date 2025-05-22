import streamlit as st

import uuid

from groq_api import chat_with_groq


st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("🤖 Chat with LLaMA 3 (via Groq)")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]
if "reset_flag" not in st.session_state:
    st.session_state.reset_flag = False

with st.sidebar:
    st.title("Settings")

    system_prompt = st.text_area(
        "System prompt:",
        value=st.session_state.messages[0]["content"],
        height=100
    )

    if system_prompt != st.session_state.messages[0]["content"]:
        st.session_state.messages[0]["content"] = system_prompt
        st.success("System prompt updated!")

    st.markdown("---")

    if st.button("🔁 Reset Chat"):
        st.session_state.reset_flag = True

if st.session_state.reset_flag:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]
    st.session_state.chat_id = str(uuid.uuid4())
    st.session_state.reset_flag = False
    st.success("Chat reset!") 

for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"], avatar="👨🏻‍💻" if msg["role"] == "user" else "🤖"):
        st.markdown(msg["content"])

user_input = st.chat_input("Say something...")

if user_input:
    with st.chat_message("user", avatar="👨🏻‍💻"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Groq is thinking..."):
            try:
                reply = chat_with_groq(st.session_state.messages)
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error(f"Error: {e}")
