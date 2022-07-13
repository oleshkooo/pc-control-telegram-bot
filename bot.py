import telebot
import os

# TODO get token from user 
TOKEN = "5428408141:AAFpzz6uw7VmMyVyqsKiOm5VhZehDFFRGOk"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello, I am a bot")

# @bot.message_handler(commands = ['help'])


# @bot.message_handler(content_types = 'text



bot.polling(none_stop = True)