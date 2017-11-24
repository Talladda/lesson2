from telegram.ext import Updater, CommandHandler, MessageHandler, Filters #импортирует нужные компоненты
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
def new_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Вызван /start')
def talk_to_me(bot, update):
    user_text = update.message.text
    logging.info(user_text)
    update.message.reply_text(user_text)
def main():
    updater = Updater("489495136:AAG1YomFQgzb7sDMMXrYkAaGcVSP26t7ZWg")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", new_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling() #ходит и спрашивает телеграм - есть что для меня?
    updater.idle() #Ходить до тех пор, пока его не остановят
main()
