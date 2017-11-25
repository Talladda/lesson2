from telegram.ext import Updater, CommandHandler, MessageHandler, Filters #импортирует нужные компоненты
import logging
import ephem
import datetime
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
def count(bot, update, args):
    user_text = update.message.text
    print(user_text.split(' ').count)
def planets(first):
    if first in ephem.Planet:
    ephem.constellation(first)
planets(input ("Enter the name of planet: "))
def main():
    updater = Updater("489495136:AAG1YomFQgzb7sDMMXrYkAaGcVSP26t7ZWg")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", new_user))
    dp.add_handler(CommandHandler("planets", first))
    dp.add_handler(CommandHandler("wordcount", count))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling() #ходит и спрашивает телеграм - есть что для меня?
    updater.idle() #Ходить до тех пор, пока его не остановят
main()
