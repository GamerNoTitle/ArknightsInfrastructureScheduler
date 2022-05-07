import os
import sys

if sys.platform == 'win32':
    adb = './adb/adb.exe'
else:
    adb = './adb/adb'

command_head = f'{adb} shell '

def touch(pos):
    pos_x, pos_y = pos[0], pos[1]
    try:
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