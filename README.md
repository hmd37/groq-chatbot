# 🚀 Groq Chatbot: Chat with LLaMA 3 - Your AI Sidekick! 🤖

---

## ✨ Overview

Welcome to your personal AI companion! This interactive chatbot, crafted with **Streamlit**, lets you dive into conversations with the powerful **LLaMA 3 language model**, supercharged by Groq's blazing-fast API. Get ready for a smooth, responsive, and customizable chat experience! 💬

---

## 🌟 Features

* **⚡️ LLaMA 3 Integration**: Experience lightning-fast responses from the LLaMA 3 model, thanks to Groq's cutting-edge inference engine. It's like having a super-speedy brain at your fingertips! 🧠💨
* **🎨 Customizable Themes**: Express yourself! Choose from "Default" 🌟, "Professional" 👔, and "Fun" 🎉 themes to match your mood and personalize the chatbot's look and feel.
* **📝 System Prompt Presets**: Need a coding buddy? A creative muse? A math whiz? Instantly switch between diverse system prompt presets (e.g., "General Assistant," "Code Assistant," "Creative Writer") or craft your very own custom persona! 🎭
* **📜 Chat History**: Never lose your train of thought! Your entire conversation history is seamlessly preserved within your session. 📖
* **🔄 Reset Chat**: Ready for a fresh start? A single click clears the slate, letting you embark on a brand new conversational journey. ✨
* **✨ Dynamic Styling**: Watch your messages come to life! All chat bubbles are dynamically styled with delightful backgrounds and fonts based on your chosen theme, making every interaction a pleasure to read. 🌈

---

## 🚀 Getting Started - Let's Get You Chatting!

Follow these simple steps to bring your Groq Chatbot to life. It's quick, easy, and rewarding! 👇

### 📋 Prerequisites

Before we embark on this exciting adventure, make sure you have these essentials:

* **Python 3.8+**: Our chatbot loves a modern Python environment. 🐍
* **Groq API Key**: This is your golden ticket! 🎟️ You'll need an API key from Groq to unleash the power of LLaMA 3. Sign up and grab yours from the [Groq website](https://groq.com/).

### 📦 Installation

1.  **Clone the repository (or grab the code):**
    If you've got the code as a file, just skip to the next step. If it's part of a Git repo, let's clone it first:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a virtual environment (highly recommended for a clean setup!):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    Our app relies on `streamlit` for its beautiful UI and `groq` for connecting to the AI magic.
    ```bash
    pip install streamlit groq
    ```

### 🔑 Configuration - Your API Key is Key!

1.  **Set your Groq API Key:**
    The application expects a file named `groq_api.py` with a `chat_with_groq` function. Inside this file, you'll securely store your Groq API key. **For top-notch security, always use environment variables for your API keys!** 🔒

    Create a file named `groq_api.py` in the same directory as your main app file (e.g., `app.py`). Paste this content into it:

    ```python
    import os
    from groq import Groq

    def chat_with_groq(messages):
        # Retrieve API key from environment variable for security
        client = Groq(api_key=os.environ.get("GROQ_API_KEY")) 
        # You could also directly paste your key here for quick testing: "gsk_..."
        
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama3-8b-8192", # Or another LLaMA 3 model you prefer!
        )
        return chat_completion.choices[0].message.content
    ```

    **🚨 Important! Before launching the app, set your `GROQ_API_KEY` environment variable:**

    * **🐧 Linux/macOS:**
        ```bash
        export GROQ_API_KEY="your_super_secret_groq_api_key_here"
        ```
    * **🖥️ Windows (Command Prompt):**
        ```cmd
        set GROQ_API_KEY="your_super_secret_groq_api_key_here"
        ```
    * **⚡️ Windows (PowerShell):**
        ```powershell
        $env:GROQ_API_KEY="your_super_secret_groq_api_key_here"
        ```
    Remember to replace `"your_super_secret_groq_api_key_here"` with your actual API key.

### ▶️ Running the Application - Lights, Camera, Chat!

1.  **Navigate to the directory** where your main application file resides (e.g., `app.py`).

2.  **Launch the Streamlit app:**
    ```bash
    streamlit run your_app_file_name.py
    ```
    (Don't forget to replace `your_app_file_name.py` with the actual name of your Python file containing the Streamlit code!)

3.  Your web browser should magically pop open to the Streamlit application. If it's playing shy, just open your browser and head to `http://localhost:8501`. 🌐

---

## 💡 How to Use - Your Chat, Your Rules!

1.  **🗣️ Start Chatting**: Type your brilliant thoughts into the "Say something..." input box at the bottom and hit Enter or click the send button.
2.  **🌈 Change Theme**: Feeling colorful? Use the "Choose Theme" dropdown in the sidebar to effortlessly switch between "Default," "Professional," and "Fun" vibes.
3.  **🎯 Select Prompt Preset**: Instantly transform your AI! Use the "Choose a prompt preset:" dropdown in the sidebar to load a pre-defined system prompt tailored for various tasks.
4.  **✍️ Custom System Prompt**: Want to fine-tune your AI's personality? Adjust the "System prompt:" text area in the sidebar. Your changes take effect immediately!
5.  **♻️ Reset Chat**: Need a clean slate? Click the "🔁 Reset Chat" button in the sidebar to clear the conversation history and begin a brand new dialogue.

---

## 📂 Project Structure

Here's how your project files will look:
├── your_app_file_name.py  # The heart of your Streamlit chatbot 💖
├── groq_api.py            # The brains of the operation, handling Groq API calls 🧠
└── README.md              # You're reading it! Project guide and instructions 📝


---

## 🤝 Contributing - Join the Fun!

Got ideas? Found a bug? We'd love your help! Feel free to fork this repository, propose improvements, or submit pull requests. Let's build something awesome together! 🚀

---

## 📄 License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT). Freedom to explore and innovate! 🔓

---
