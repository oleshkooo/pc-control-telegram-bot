
#* Тимчасова версія введення даних до програми через консоль
#* Після створення графічного інтерфейсу потрібно замінити введення даних

import os
import telebot
import pickle
import atexit
from os.path import abspath

class Data:
    def __init__(self):
        self.ID = None
        self.TOKEN = None


#!!! Якшо юзати прогу, для коректної роботи необхідно дадати одну крапку ->> -| '../' |- )
#!!! Для компіляції використовувати './'
#!              |
#!              V        
PATH = abspath('../') + '\\data\\data.bin'
flag = False

def readFromFile():
    file = open(PATH, 'rb')
    user = pickle.load(file)
    file.close()
    return user


#! Якшо токен введено не коректоно то програ крашнеться. Треба придумати якусь перевірку на коректність токена та ID

def inputProcess():
    global flag
    user = Data()
       
    while not flag:    
        user.ID = input('[BOT] Enter your ID >>> ')
        user.TOKEN = input('[BOT] Enter bot TOKEN >>> ')
        bot = telebot.TeleBot(user.TOKEN)
        if bot and user.ID.isdigit():
            user.ID = int(user.ID)
            bot.stop_polling()
            flag = True
            break
        print('⛔ Incorrect ID or token\n')

    file = open(PATH, 'wb')
    pickle.dump(user, file)
    file.close()
    return user

def getData():
    if os.path.exists(PATH):
        user = readFromFile()
    else:
        user = inputProcess()
    return user

# def exitHandler():
#     if not flag:
#         os.remove(PATH)

# atexit.register(exitHandler)