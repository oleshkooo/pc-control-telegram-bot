
#* Тимчасова версія введення даних до програми через консоль
#* Після створення графічного інтерфейсу потрібно замінити введення даних

import os
import telebot
import pickle
import atexit
from os.path import abspath


class Data:
    def __init__(self):
        self.users = []
        self.TOKEN = ''


#!!! Якшо юзати прогу, для коректної роботи необхідно дадати одну крапку ->> -| '../' |- )
#!!! Для компіляції використовувати './'
#!              |
#!              V        
PATH = abspath('../') + '\\data\\data.bin'

def readFromFile():
    file = open(PATH, 'rb')
    data = pickle.load(file)
    file.close()
    return data


#! Якшо токен введено не коректоно то програ крашнеться. Треба придумати якусь перевірку на коректність токена та ID

def inputProcess():

    data = Data()


    while True:
        username = input('[BOT] Enter permitted username (type \'-\' to stop) >>> ')
        if username != '-':
            data.users.append(username)
        elif username == '-' and len(data.users) > 0: 
            break

    while True:
        data.TOKEN = input('\n[BOT] Enter bot TOKEN >>> ')
        bot = telebot.TeleBot(data.TOKEN)
        if bot:
            bot.stop_polling()
            break
        print('⛔ Incorrect Token\n')

    file = open(PATH, 'wb')
    pickle.dump(data, file)
    file.close()
    return data

def getData():
    if os.path.exists(PATH):
        data = readFromFile()
    else:
        data = inputProcess()
    return data