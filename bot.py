from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters

import config as key
import responses as R

async def handle_message(update: Update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    await update.message.reply_text(response)

WELCOME_MESSAGE = "Hi! Welcome to the bot. How can I assist you today?"

async def start_handler(update: Update, context):
    keyboard = get_main_keyboard()
    await update.message.reply_text(WELCOME_MESSAGE, reply_markup = keyboard, disable_web_page_preview = True)

async def phone_handler(update: Update, context):
    keyboard = [[KeyboardButton(text = "Send phone", request_contact = True)]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True, one_time_keyboard = True)
    await update.message.reply_text("Phone number", reply_markup = reply_markup)

async def contact_handler(update: Update, context):
    if update.message.contact is not None:
        print(update.message.contact)

def get_main_keyboard():
    keyboard = [
        [KeyboardButton(text = "hello")],
        [KeyboardButton(text = "fine")],
        [KeyboardButton(text = "how are you?")],
        [KeyboardButton(text = "who are you?")],
        [KeyboardButton(text = "what is the time?")],
    ]

    markup = ReplyKeyboardMarkup(keyboard, resize_keyboard = True)
    return markup

async def error(update: Update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    # Create the application
    application = Application.builder().token(key.TG_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("help", start_handler))
    application.add_handler(CommandHandler("number", phone_handler))
    application.add_handler(MessageHandler(filters.CONTACT, contact_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
