from os import path as os_path
from sys import executable
from json import load as json_load

def readJSSON(path):
    filename = os_path.join(os_path.dirname(executable), 'myfilename.tga')
    # file = open(os_path.dirname(__file__) + path)
    fileJSON = json_load(file)
    return fileJSON