import os
import sys
import time

if sys.platform == 'win32':
    adb = '".\\adb\\platform-tools\\adb.exe"'
else:
    adb = './adb/platform-tools/adb'

command_head = f'{adb} shell '


class device():
    def __init__(self, address, port, logger):
        self.address = address
        self.port = port
        self.logger = logger

    def touch(self, result_set):
        ([x1, y1], [x2, y2], string) = (result_set[0]
                                        [0], result_set[0][2], result_set[1][0])
        pos_x, pos_y = (x1+x2)/2, (y1+y2)/2
        try:
            self.logger.info(f'Try to touch {pos_x} {pos_y}, string: {string}')
            self.logger.info(os.popen(f'{command_head}input tap {pos_x} {pos_y}').read())
        except:
            raise RuntimeWarning(
                'This tap operation is failed to push to the device.')

    def slide(self, start, end):
        start_x, start_y = start[0], start[1]
        end_x, end_y = end[0], end[1]
        try:
            self.logger.info(os.popen(
                f'{command_head}input swipe {start_x} {start_y} {end_x} {end_y}').read())
        except:
            raise RuntimeWarning(
                'This slide operation is failed to push to the device.')

    def back(self):
        try:
            self.logger.info(os.popen(f'{command_head}input keyevent 3').read())
        except:
            raise RuntimeWarning(
                'This back operation is failed to push to te device.')

    def connect(self, address: str, port: int):
        try:
            self.logger.info(os.popen(f'{adb} connect {address}:{port}').read())
        except:
            raise RuntimeWarning('Cannot connect to the device.')

    def restart(self):
        try:
            self.logger.info(os.popen(f'{adb} kill-server').read())
            self.logger.info(os.popen(f'{adb} start-server').read())
        except:
            raise RuntimeWarning('Cannot restart the adb server.')

    def devices(self):
        try:
            self.logger.info(os.popen(f'{adb} devices').read())
        except:
            raise RuntimeWarning('Cannot fetch device info.')

    def screencapture(self, temp_dir: str):
        filename = f'{time.strftime("%Y%m%d%H%M%S")}.png'
        if sys.platform == 'win32':
            commands = f'''{adb} shell screencap -p /sdcard/temp.png
            {adb} pull /sdcard/temp.png {temp_dir}\\{filename}.png
            {adb} shell rm /sdcard/temp.png'''
            for i in commands.split('\n'):
                self.logger.info(os.popen(f'{i}').read())
            return f'{temp_dir}\\{filename}.png'
        else:
            commands = f'''{adb} shell screencap -p /sdcard/temp.png
            {adb} pull /sdcard/temp.png {temp_dir}/{filename}.png
            {adb} shell rm /sdcard/temp.png'''
            for i in commands.split('\n'):
                self.logger.info(os.popen(f'{i}').read())
            return f'{temp_dir}/{filename}.png'
