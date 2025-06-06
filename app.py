import streamlit as st

from src.chat_handler import handle_user_input
from src.message_display import display_chat_history
from src.sidebar import setup_sidebar
from src.utils import apply_theme_styles, initialize_session_state

st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("🤖 Chat with LLaMA 3 (via Groq)")

initialize_session_state()
system_prompt = setup_sidebar()
avatars, _ = apply_theme_styles()

if st.session_state.reset_flag:
    import uuid
    st.session_state.messages = [{"role": "system", "content": system_prompt}]
    st.session_state.chat_id = str(uuid.uuid4())
    st.session_state.reset_flag = False
    st.success("Chat reset!")

display_chat_history(avatars)
handle_user_input(avatars)
