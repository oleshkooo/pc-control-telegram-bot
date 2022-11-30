from os import path as os_path
from pathlib import Path as pathlibPath
from pickle import load as picke_load, dump as pickle_dump
from json import load as json_load


def writeToFile(data):
    # config = open(os_path.dirname(__file__) + '/../config.json')
    # configJSON = json_load(config)
    # path = os_path.expanduser('~') + configJSON['cachePath'] + configJSON['cacheFile']
    PATH = os_path.expanduser('~') + '\\AppData\\Local\\PC_Control_Bot\\data.bin'

    if not os_path.exists(PATH):
        pPath = pathlibPath(PATH)
        pPath.parent.mkdir(parents=True, exist_ok=True)

    with open(PATH, 'wb') as file:
        pickle_dump(data, file)
