import textwrap
from io import BytesIO

import streamlit as st
from gtts import gTTS


def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]
    if "reset_flag" not in st.session_state:
        st.session_state.reset_flag = False
    if "theme" not in st.session_state:
        st.session_state.theme = "Default"

def setup_sidebar():
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

        return system_prompt

def apply_theme_styles():
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

    return avatars, style

def styled_message(role, content):
    css_class = "user-message" if role == "user" else "bot-message"
    return f'<div class="{css_class}">{content}</div>'

def split_text(text, max_chars=200):
    return textwrap.wrap(text, max_chars, break_long_words=False, replace_whitespace=False)

def play_response_audio(text, max_chars=200):
    chunks = split_text(text, max_chars)
    for chunk in chunks:
        tts = gTTS(chunk)
        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        st.audio(audio_buffer, format="audio/mp3")
