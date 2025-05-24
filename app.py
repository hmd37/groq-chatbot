import streamlit as st

import uuid

from groq_api import chat_with_groq

st.set_page_config(page_title="Groq Chatbot", page_icon="🤖")
st.title("🤖 Chat with LLaMA 3 (via Groq)")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]
if "reset_flag" not in st.session_state:
    st.session_state.reset_flag = False
if "theme" not in st.session_state:
    st.session_state.theme = "Default"

with st.sidebar:
    st.title("Settings")

    theme = st.selectbox("Choose Theme", ["Default", "Professional", "Fun"], index=["Default", "Professional", "Fun"].index(st.session_state.theme))
    st.session_state.theme = theme

    preset_prompts = {
        "General Assistant": "You are a helpful assistant.",
        "Code Assistant": "You are a coding assistant. Provide clean, commented code and explain it clearly.",
        "Creative Writer": "You are a creative writing assistant. Help with stories, poems, and plot ideas.",
        "Math Tutor": "You are a math tutor. Explain concepts step-by-step in simple terms.",
        "Travel Planner": "You are a travel planner. Help suggest destinations and itineraries."
    }

    selected_preset = st.selectbox("Choose a prompt preset:", options=list(preset_prompts.keys()))
    default_prompt = preset_prompts[selected_preset]

    system_prompt = st.text_area(
        "System prompt:",
        value=default_prompt,
        height=100,
        key="system_prompt_input"
    )

    if system_prompt != st.session_state.messages[0]["content"]:
        st.session_state.messages[0]["content"] = system_prompt
        st.success("System prompt updated!")

    st.markdown("---")

    if st.button("🔁 Reset Chat"):
        st.session_state.reset_flag = True

theme_avatars = {
    "Default": {"user": "👨🏻‍💻", "bot": "🤖"},
    "Professional": {"user": "🧑‍💼", "bot": "📊"},
    "Fun": {"user": "😎", "bot": "🎉"},
}
avatars = theme_avatars.get(st.session_state.theme, theme_avatars["Default"])

theme_styles = {
    "Default": {
        "font_family": "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
        "user_bg": "#e6f0ff",
        "bot_bg": "#f0f0f0",
        "font_color": "#000000"
    },
    "Professional": {
        "font_family": "'Times New Roman', Times, serif",
        "user_bg": "#d1e7dd",
        "bot_bg": "#badbcc",
        "font_color": "#0f5132"
    },
    "Fun": {
        "font_family": "'Comic Sans MS', cursive, sans-serif",
        "user_bg": "#fff3cd",
        "bot_bg": "#ffeeba",
        "font_color": "#856404"
    }
}
style = theme_styles.get(st.session_state.theme, theme_styles["Default"])

st.markdown(f"""
    <style>
        .user-message {{
            background-color: {style['user_bg']};
            padding: 10px 15px;
            border-radius: 15px;
            max-width: 80%;
            font-family: {style['font_family']};
            color: {style['font_color']};
            margin-bottom: 8px;
        }}
        .bot-message {{
            background-color: {style['bot_bg']};
            padding: 10px 15px;
            border-radius: 15px;
            max-width: 80%;
            font-family: {style['font_family']};
            color: {style['font_color']};
            margin-bottom: 8px;
        }}
    </style>
""", unsafe_allow_html=True)

def styled_message(role, content):
    if role == "user":
        return f'<div class="user-message">{content}</div>'
    else:
        return f'<div class="bot-message">{content}</div>'

if st.session_state.reset_flag:
    st.session_state.messages = [{"role": "system", "content": system_prompt}]
    st.session_state.chat_id = str(uuid.uuid4())
    st.session_state.reset_flag = False
    st.success("Chat reset!")

for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"], avatar=avatars["user"] if msg["role"] == "user" else avatars["bot"]):
        st.markdown(styled_message(msg["role"], msg["content"]), unsafe_allow_html=True)

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
                st.session_state.messages.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error(f"Error: {e}")
