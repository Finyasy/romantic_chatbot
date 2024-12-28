from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
from telegram.ext import filters as Filters


from chat_handler import romantic_chat

TELEGRAM_TOKEN = "YOUR_TELEGRAM"

def handle_message(update: Update, context: CallbackContext):
    user_input = update.message.text
    bot_reply = romantic_chat(user_input)
    update.message.reply_text(bot_reply)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I'm a romantic chatbot. What's on your mind?")

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("Bot is running!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()