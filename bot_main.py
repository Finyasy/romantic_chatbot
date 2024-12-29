import os
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, MessageHandler
from telegram.ext import filters as Filters
from telegram.ext import Application
from dotenv import load_dotenv
from chat_handler import romantic_chat

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TELEGRAM_TOKEN:
    raise ValueError("No TELEGRAM_TOKEN found in environment variables")

async def handle_message(update: Update, context: CallbackContext):
    user_input = update.message.text
    bot_reply = await romantic_chat(user_input)
    await update.message.reply_text(bot_reply)

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I'm a romantic chatbot. What's on your mind?")

def main():

    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(Filters.TEXT & ~Filters.COMMAND, handle_message))

    print("Bot is running!")
    application.run_polling()

if __name__ == "__main__":
    main()