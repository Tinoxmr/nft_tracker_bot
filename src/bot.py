import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from tracker import get_token_info

telegram_bot_token = "1802801646:AAG2kdFBEOF2dsBylMdUi9uBcFsa_GbKtD0"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Hello, this bot tracks token #8713 from BMWU contract")


def info(update, context):
    response = get_token_info()
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text=response)


dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("info", info))
updater.start_polling()