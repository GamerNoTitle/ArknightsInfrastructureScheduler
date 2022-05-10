import os
import threading as t
import json

from utils import adb
from utils.Initalize import Initalize
from utils.Ocr import recongnize
from utils.PropertiesParser import parse

class RunningError(Exception):
    pass

with open('./config.json', 'rt') as f:
    config = json.loads(f.read())

if __name__ == '__main__':
    if not os.path.exists('./adb'): 
        DownloadProgress = t.Thread(target=Initalize, name='Initalize')
        DownloadProgress.run()
        DownloadProgress.join()
    # Connect to the device
    if config['bluestacks']['enable']:
        port = int(parse(config['bluestacks']['conf']).get('bst.instance.Nougat64.status.adb_port', '5555').replace('"',''))
        adb.restart()
        adb.connect('127.0.0.1', port)
    else:
        address = config['address']
        port = config['port']
        adb.restart()
        adb.connect(address, port)
    # Connect Completed
    file = adb.screencapture()
    try:
        result = recongnize(file)
        print(result)
    except FileNotFoundError:
        raise RunningError('Could not find the screen captured picture.')
    