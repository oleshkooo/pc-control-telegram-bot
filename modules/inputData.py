import os
import pickle
import ctypes

class Data:
    def __init__(self):
        self.USER = ''
        self.TOKEN = ''
        self.dict = {}

def getData():
    MessageBox = ctypes.windll.user32.MessageBoxW
    PATH = os.path.expanduser('~') + '\\AppData\\Local\\PC Control Bot Data\\data.bin'
    if os.path.exists(PATH): 
        file = open(PATH, 'rb')
        data = pickle.load(file)
        if data.USER == None and data.TOKEN == None:
            MessageBox(0, "ERROR: Token and Username not found\n Please enter your Username and Token in the settings", "PC Control Bot", 0)
            return None
        elif data.USER == None:
            MessageBox(0, "ERROR: Username not found\n Please enter your Username in the settings", "PC Control Bot", 0)
            return None
        elif data.TOKEN == None:
            MessageBox(0, "ERROR: Token not found\n Please enter your Token in the settings", "PC Control Bot", 0)
            return None
        file.close()
        return data

    MessageBox(None,'ERROR: no data found\nEnter the data in the program!' , 'PC Control Bot', 0)
    return None