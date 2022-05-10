import os
import sys
from tempfile import TemporaryFile

if sys.platform == 'win32':
    adb = '".\\adb\\platform-tools\\adb.exe"'
else:
    adb = './adb/platform-tools/adb'

command_head = f'{adb} shell '

class device():
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.restart()
        self.connect(self.address, self.port)

    def touch(result_set):
        ([x1, y1], [x2, y2], string) = (result_set[0][0], result_set[0][2], result_set[1][0])
        pos_x, pos_y = (x1+x2)/2, (y1+y2)/2
        try:
            print(f'Try to touch {pos_x} {pos_y}, string: {string}')
            os.system(f'{command_head}input tap {pos_x} {pos_y}')
        except:
            raise RuntimeWarning('This tap operation is failed to push to the device.')

    def slide(start, end):
        start_x, start_y = start[0], start[1]
        end_x, end_y = end[0], end[1]
        try:
            os.system(f'{command_head}input swipe {start_x} {start_y} {end_x} {end_y}')
        except:
            raise RuntimeWarning('This slide operation is failed to push to the device.')

    def back():
        try:
            os.system(f'{command_head}input keyevent 3')
        except:
            raise RuntimeWarning('This back operation is failed to push to te device.')

    def connect(address: str, port: int):
        try:
            os.system(f'{adb} connect {address}:{port}')
        except:
            raise RuntimeWarning('Cannot connect to the device.')

    def restart():
        try:
            os.system(f'{adb} kill-server')
            os.system(f'{adb} start-server')
        except:
            raise RuntimeWarning('Cannot restart the adb server.')

    def devices():
        try:
            os.system(f'{adb} devices')
        except:
            raise RuntimeWarning('Cannot fetch device info.')

    def screencapture():
        commands = f'''{adb} shell screencap -p /sdcard/temp.png
        {adb} pull /sdcard/temp.png ./temp.png
        {adb} shell rm /sdcard/temp.png'''
        for i in commands.split('\n'):
            os.system(f'{i}')
        return f'temp.png'