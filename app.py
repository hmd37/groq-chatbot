import streamlit as st
from groq_api import chat_with_groq

# Page settings
st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("🤖 Chat with LLaMA 3 (via Groq)")


# Session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Display chat messages with avatars
for msg in st.session_state.messages[1:]:  # Skip system prompt
    with st.chat_message(msg["role"], avatar="🧑" if msg["role"] == "user" else "🤖"):
        st.markdown(msg["content"])

# Chat input box
user_input = st.chat_input("Say something...")

if user_input:
    # Show user message
    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response from Groq model
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Groq is thinking..."):
            try:
                reply = chat_with_groq(st.session_state.messages)
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error(f"Error: {e}")
