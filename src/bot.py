import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from tracker import get_token_info
from sales_tracker import get_lasthour_sales


telegram_bot_token = "1802801646:AAG2kdFBEOF2dsBylMdUi9uBcFsa_GbKtD0"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="Hello, this bot tracks the number of hourly sales for the SPOOKIES nft")
    context.job_queue.run_repeating(callback_minute, interval=3600, first=2, context=update.message.chat_id)


def callback_minute(context):
    chat_id = context.job.context
    n = get_lasthour_sales()
    text = 'SPOOKIES sales in the last hour: ' + str(n)
    context.bot.send_message(chat_id=chat_id, text=text)


def info(update, context):
    response = get_token_info()
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text=response)


dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()
