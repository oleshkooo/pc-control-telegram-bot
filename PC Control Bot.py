import subprocess
import psutil
import ctypes
import sys

for proc in psutil.process_iter():
        if proc.name() == "GUI.exe":
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(0, "PC Control Bot is already running", "PC Control Bot", 0)
            sys.exit()


subprocess.call('cd GUI && GUI.exe', shell = True)
