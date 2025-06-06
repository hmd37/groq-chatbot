from groq import Groq

from src.config import GROQ_API_KEY, MODEL

client = Groq(api_key=GROQ_API_KEY)


def chat_with_groq(messages, temperature=0.7):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content
