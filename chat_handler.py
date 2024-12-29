import asyncio
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPEN_AI_API_KEY is not set in the environment variables.")

client = OpenAI(api_key=api_key)

chat_history = []

async def romantic_chat(user_input):
    global chat_history
    chat_history.append(f"User: {user_input}")

    context = "\n".join(chat_history[-5:])

    try:
        response = await asyncio.to_thread(
            client.chat.completions.create,
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a romantic chatbot."},
                *[{"role": "user", "content": msg} for msg in chat_history]
            ],
            max_tokens=100,
            temperature=0.7
        )

        print("OpenAI Response:", response)

        if response.choices and len(response.choices) > 0:
            bot_reply = response.choices[0].message.content.strip()
            if bot_reply:
                chat_history.append(f"Bot: {bot_reply}")
                return bot_reply
            else:
                return "I'm sorry, I couldn't generate a response."
        else:
            return "No valid response from OpenAI."

    except Exception as e:
        print(f"Error during OpenAI API call: {e}")
        return "Something went wrong. Please try again later."

async def handle_message(update, context):
    user_input = update.message.text
    bot_reply = await romantic_chat(user_input)

    if bot_reply:
        await update.message.reply_text(bot_reply)
    else:
        await update.message.reply_text("Sorry, I couldn't think of a reply.")
