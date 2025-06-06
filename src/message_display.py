import streamlit as st

from utils import styled_message


def display_chat_history(avatars):
    for msg in st.session_state.messages[1:]:
        with st.chat_message(msg["role"], avatar=avatars["user"] if msg["role"] == "user" else avatars["bot"]):
            st.markdown(styled_message(msg["role"], msg["content"]), unsafe_allow_html=True)
