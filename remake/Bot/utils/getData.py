from os import ( path as os_path, remove as os_remove )
from pathlib import Path as pathlibPath
from pickle import load as pickle_load
from json import load as json_load
from ctypes import windll



def getData():
    MessageBox = windll.user32.MessageBoxW
    # config = open(os_path.dirname(__file__) + '/../config.json')
    # configJSON = json_load(config)
    # path = os_path.expanduser('~') + configJSON['cachePath'] + configJSON['cacheFile']
    path = os_path.expanduser('~') + '\\AppData\\Local\\PC_Control_Bot\\data.bin'

    if not os_path.exists(path):
        MessageBox(0, 'ERROR: Cache file not found', 'PC Control Bot', 0)
        return None

    file = open(path, 'rb')
    data = pickle_load(file)

    if data.USERNAME == None and data.TOKEN == None:
        MessageBox(0, 'ERROR: Token and Username not found\n Please enter your Username and Token in the settings', "PC Control Bot", 0)
        return None

    if data.USERNAME == None:
        MessageBox(0, 'ERROR: Username not found\n Please enter your Username in the settings', "PC Control Bot", 0)
        return None

    if data.TOKEN == None:
        MessageBox(0, 'ERROR: Token not found\n Please enter your Token in the settings', "PC Control Bot", 0)
        return None

    file.close()
    return data