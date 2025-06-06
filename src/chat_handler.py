import streamlit as st

from groq_api import chat_with_groq
from utils import play_response_audio, styled_message


def handle_user_input(avatars):
    user_input = st.chat_input("Say something...")

    if user_input:
        with st.chat_message("user", avatar=avatars["user"]):
            st.markdown(styled_message("user", user_input), unsafe_allow_html=True)
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("assistant", avatar=avatars["bot"]):
            with st.spinner("Groq is thinking..."):
                try:
                    reply = chat_with_groq(st.session_state.messages)
                    st.markdown(styled_message("assistant", reply), unsafe_allow_html=True)
                    play_response_audio(reply)
                    st.session_state.messages.append({"role": "assistant", "content": reply})
                except Exception as e:
                    st.error(f"Error: {e}")
