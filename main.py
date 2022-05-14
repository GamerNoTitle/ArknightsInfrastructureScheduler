import os
import threading
import json
import time
from pprint import pformat, pprint


from utils.adb import device
from utils.Initalize import Initalize
from utils.Ocr import recongnize
from utils.PropertiesParser import parse
from utils.Logger import logger

from tasks import Infrastructure

class RunningError(Exception):
    pass


with open('./config.json', 'rt') as f:
    config = json.loads(f.read())

if __name__ == '__main__':
    t = time.localtime(time.time())
    mo = str(t.tm_mon) if len(str(t.tm_mon)) == 2 else '0' + str(t.tm_mon)
    day = str(t.tm_mday) if len(str(t.tm_mday)) == 2 else '0' + str(t.tm_mday)
    hour = str(t.tm_hour) if len(str(t.tm_hour)) == 2 else '0' + str(t.tm_hour)
    minute = str(t.tm_min) if len(str(t.tm_min)) == 2 else '0' + str(t.tm_min)
    log_file = f'./logs/{t.tm_year}-{mo}-{day}-{hour}-{minute}.log'
    log = logger(config['log_level'].upper(), log_file) if config['log_level'].upper() in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'] else 'INFO'
    if not os.path.exists('./adb'):
        DownloadProgress = threading.Thread(target=Initalize, name='Initalize', args=(log,))
        DownloadProgress.run()
    temp_dir = 'cache'

    # Connect to the device
    if config['bluestacks']['enable']:
        port = int(parse(config['bluestacks']['conf'], log).get(
            'bst.instance.Nougat64.status.adb_port', '5555').replace('"', ''))
        emulator = device('127.0.0.1', port, log)
        emulator.restart()
        emulator.connect(emulator.address, emulator.port)
    else:
        address = config['address']
        port = config['port']
        emulator = device(address, port)
        emulator.restart()
        emulator.connect(emulator.address, emulator.port)
    # Connect Completed

    file = emulator.screencapture(temp_dir)
    try:
        result = recongnize(file, logger)
        log.info(result)
    except FileNotFoundError:
        log.warn('Could not find the screen captured picture.')

    # Testing Operation
    # result = [[[[1864.0, 8.0], [1908.0, 8.0], [1908.0, 32.0], [1864.0, 32.0]], ('8:50', 0.9083485007286072)], [[[162.0, 149.0], [220.0, 149.0], [220.0, 179.0], [162.0, 179.0]], ('a', 0.6850617527961731)], [[[1069.0, 152.0], [1151.0, 157.0], [1149.0, 187.0], [1067.0, 182.0]], ('biubiu', 0.9640132784843445)], [[[1366.0, 163.0], [1460.0, 163.0], [1460.0, 214.0], [1366.0, 214.0]], ('bilibili', 0.776603639125824)], [[[1663.0, 166.0], [1728.0, 160.0], [1731.0, 190.0], [1666.0, 195.0]], ('SST', 0.7298862934112549)], [[[160.0, 248.0], [254.0, 248.0], [254.0, 278.0], [160.0, 278.0]], ('系统应用', 0.9993674755096436)], [[[460.0, 248.0], [554.0, 248.0], [554.0, 278.0], [460.0, 278.0]], ('蔚蓝檔案', 0.9363634586334229)], [[[762.0, 248.0], [856.0, 248.0], [856.0, 278.0], [762.0, 278.0]], ('明日方舟', 0.9336056709289551)], [
    #     [[1046.0, 250.0], [1174.0, 250.0], [1174.0, 278.0], [1046.0, 278.0]], ('biubiu加速器', 0.9443848729133606)], [[[1354.0, 252.0], [1474.0, 252.0], [1474.0, 274.0], [1354.0, 274.0]], ('哔哩哔哩HD', 0.7773469090461731)], [[[1636.0, 248.0], [1790.0, 250.0], [1790.0, 278.0], [1636.0, 276.0]], ('Packet Capture', 0.948020339012146)], [[[464.0, 395.0], [550.0, 395.0], [550.0, 441.0], [464.0, 441.0]], ('bilibili', 0.8801730871200562)], [[[158.0, 478.0], [250.0, 478.0], [250.0, 508.0], [158.0, 508.0]], ('明日计划', 0.9971569776535034)], [[[462.0, 478.0], [554.0, 478.0], [554.0, 506.0], [462.0, 506.0]], ('哔哩哔哩', 0.7854729890823364)], [[[770.0, 478.0], [846.0, 478.0], [846.0, 508.0], [770.0, 508.0]], ('云·原神', 0.9809289574623108)], [[[1042.0, 476.0], [1180.0, 476.0], [1180.0, 510.0], [1042.0, 510.0]], ('明日方舟速通', 0.9849907755851746)]]
    # for i in result:
    #     time.sleep(5)
    #     device.touch(result_set = i)

    # tasks = [
    #     Infrastructure.run(emulator, recongnize, temp_dir)
    # ]

    pprint(result)