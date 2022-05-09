import os
import threading as t
from utils import adb
from utils.Initalize import Initalize
from utils.ProgressBar import download
from utils.PropertiesParser import parse

with open('./config.json', 'rt') as f:
    import json
    config = json.loads(f.read())

if __name__ == '__main__':
    if not os.path.exists('./adb'): 
        Initalize()
    # Connect to the device
    port = int(parse(config['bluestacks']['conf']).get('bst.instance.Nougat64.status.adb_port', '5555').replace('"',''))
    adb.restart()
    adb.connect('127.0.0.1', port)
    # Connect Completed