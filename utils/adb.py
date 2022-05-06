import os
import sys

if sys.platform == 'win32':
    adb = './adb/adb.exe'
else:
    adb = './adb/adb'

