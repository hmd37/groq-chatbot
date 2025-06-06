import streamlit as st


def setup_sidebar():
    st.sidebar.title("Settings")

    theme = st.sidebar.selectbox(
        "Choose Theme", 
        ["Default", "Professional", "Fun"], 
        index=["Default", "Professional", "Fun"].index(st.session_state.theme)
    )
    st.session_state.theme = theme

    preset_prompts = {
        "General Assistant": "You are a helpful assistant.",
        "Code Assistant": "You are a coding assistant. Provide clean, commented code and explain it clearly.",
        "Creative Writer": "You are a creative writing assistant. Help with stories, poems, and plot ideas.",
        "Math Tutor": "You are a math tutor. Explain concepts step-by-step in simple terms.",
        "Travel Planner": "You are a travel planner. Help suggest destinations and itineraries."
    }

    selected_preset = st.sidebar.selectbox("Choose a prompt preset:", options=list(preset_prompts.keys()))
    default_prompt = preset_prompts[selected_preset]

    system_prompt = st.sidebar.text_area(
        "System prompt:",
        value=default_prompt,
        height=100,
        key="system_prompt_input"
    )

    if system_prompt != st.session_state.messages[0]["content"]:
        st.session_state.messages[0]["content"] = system_prompt
        st.sidebar.success("System prompt updated!")

    st.sidebar.markdown("---")
    if st.sidebar.button("🔁 Reset Chat"):
        st.session_state.reset_flag = True

    return system_prompt
