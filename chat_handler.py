import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPEN_AI_API_KEY")

chat_history = []

def romantic_chat(user_input):
    global chat_history
    chat_history.append(f"User: {user_input}")

    context = "\n".join(chat_history[-5])

    response = openai.ChatCompletion.create(
        model="gpt-3.0-turbo",
        prompt=f"{context}\nBot:",
        max_tokens=100,
        temperature=0.7,
        stop=["User:", "Bot:"]
    )

    bot_reply = response.choices[0]["text"].strip()
    chat_history.append(f"Bot: {bot_reply}")
    return bot_reply
