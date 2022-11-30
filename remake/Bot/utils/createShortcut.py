import pythoncom
from win32com.client import Dispatch


def createShortcut(fileName: str, target: str, workDir: str, args: str = ''):
    pythoncom.CoInitialize()
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(fileName)
    shortcut.TargetPath = target
    shortcut.Arguments = args
    shortcut.WorkingDirectory = workDir
    shortcut.save()