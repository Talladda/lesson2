#from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
#from ephem import Planet
def planets(first):
        planet1 = ephem.Mars()
        print(exec('{0} = ephem.{0}()'.format(first)))
        print(exec('{0}'.format(first)))
        print('ephem.{0}()'.format(first))
planets(input ("Enter the name of planet: "))
def main():
    updater = Updater("489495136:AAG1YomFQgzb7sDMMXrYkAaGcVSP26t7ZWg")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", new_user))
    dp.add_handler(CommandHandler("planets", first))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling() #ходит и спрашивает телеграм - есть что для меня?
    updater.idle() #Ходить до тех пор, пока его не остановят
#main()