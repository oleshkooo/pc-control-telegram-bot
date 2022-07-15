
#* Тимчасова версія введення даних до програми через консоль
#* Після створення графічного інтерфейсу потрібно замінити введення даних

import os
import telebot
import pickle
from os.path import abspath

class Data:
    def __init__(self):
        self.ID = None
        self.TOKEN = None


#!!! Якшо компілити прогу, для коректної роботи необхідно дадати одну крапку ->> -| '../' |- )
#!              |
#!              V        
PATH = abspath('./') + '\\data\\data.bin' 

def ReadFromFile():
    file = open(PATH, 'rb')
    user = pickle.load(file)
    file.close()
    return user


#! Якшо токен введено не коректоно то програ крашнеться. Треба придумати якусь перевірку на коректність токена та ID

def InputProcess():
    file = open(PATH, 'wb')
    flag = False
    user = Data()
       
    while not flag:    
        user.ID = input('🆔 Enter your bot ID >>> ')
        user.TOKEN = input(' Enter your bot token >>> ')
        bot = telebot.TeleBot(user.TOKEN)
        if bot and user.ID.isdigit():
            user.ID = int(user.ID)
            bot.stop_polling()
            flag = True
            break
        print('⛔Incorrect ID or token\n')
    pickle.dump(user, file)
    file.close()
    return user

def GetData():
    if os.path.exists(PATH):
        user = ReadFromFile()
    else:
        user = InputProcess()
    return user