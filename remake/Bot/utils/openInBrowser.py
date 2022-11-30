from os import path as os_path
from json import load as json_load
from webbrowser import open as webbrowser_open
    # --new
    # 0: open in the same window
    # 1: open in a new window
    # 2: open in a new tab


def openInBrowser(url):
    # config = open(os_path.dirname(__file__) + '/../config.json')
    # configJSON = json_load(config)
    # webbrowser_open(url, new = configJSON['webbrowserNumber'])
    webbrowser_open(url, new = 2)