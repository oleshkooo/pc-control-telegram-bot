from pathlib import Path
import os
import subprocess
from win32com.client import Dispatch
import psutil
import ctypes
import sys

def create_shortcut(file_name: str, target: str, work_dir: str, arguments: str = ''):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(file_name)
    shortcut.TargetPath = target
    shortcut.Arguments = arguments
    shortcut.WorkingDirectory = work_dir
    shortcut.save()


for proc in psutil.process_iter():
        if proc.name() == "GUI.exe":
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(0, "PC Control Bot is already running", "PC Control Bot", 0)
            sys.exit()

PATH = os.path.expanduser('~') + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'

if not os.path.exists(PATH + 'PC Control Bot Host'):
    abs_file_name = os.path.abspath('.') + '\\host\\host.exe'
    pathToFile = Path(abs_file_name)
    
    name = 'PC Control Bot Host'

    create_shortcut(
        file_name = f"{PATH}\\{name}.lnk",
        target = str(pathToFile),
        work_dir = str(pathToFile.parent),
        arguments ='/cmd {%s} -new_console' % name,
    )        

subprocess.call('cd GUI && GUI.exe', shell = True)
