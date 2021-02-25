import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

proxy = {'proxy_url': settings.PROXY_URL, 'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print("Вызван /start")
    print(update)
    update.message.reply_text("Здравствуй, кожанный!")

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)
 
def main():
    mybot = Updater(settings.API_KEY, use_context = True, request_kwargs = proxy)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot Started!")
    mybot.start_polling()
    mybot.idle()

if __name == "__main__":
    main()
