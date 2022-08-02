import os
import subprocess
import psutil
import ctypes
import sys

for proc in psutil.process_iter():
        if proc.name() == "UI.exe":
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(0, "PC Control Bot is already running", "PC Control Bot", 0)
            sys.exit()

# PATH = os.path.expanduser('~') + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'

# if not os.path.exists(PATH + '\\host\\host.exe'):
#     pathToFile = os.path.abspath('.') + '\\host\\host.exe'  
#     subprocess.call(f'copy "{pathToFile}" "{PATH}',shell = True)
            
subprocess.call('cd UI && UI.exe', shell = True)
