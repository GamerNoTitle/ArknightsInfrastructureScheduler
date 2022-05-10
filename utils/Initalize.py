import os
import zipfile
import time
import sys

from utils.ProgressBar import download

adb_dl_url_windows = 'https://dl.google.com/android/repository/platform-tools-latest-windows.zip?hl=zh-cn'
adb_dl_url_linux = 'https://dl.google.com/android/repository/platform-tools-latest-linux.zip?hl=zh-cn'


def Initalize():
    if not os.path.exists('./adb'):
        os.system('mkdir adb')
    if sys.platform == 'win32':
        download(adb_dl_url_windows, './adb/platform-tools-latest-windows.zip', headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
        with zipfile.ZipFile('./adb/platform-tools-latest-windows.zip', 'r') as adbzip:
            adbzip.extractall(path='./adb')
        os.system('rm -f "./adb/platform-tools-latest-windows.zip"')
    else:
        download(adb_dl_url_linux, './adb/platform-tools-latest-linux.zip', headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
        with zipfile.ZipFile('./adb/platform-tools-latest-linux.zip', 'r') as adbzip:
            adbzip.extractall(path='./adb')
        os.system('rm -rf "./adb/platform-tools-latest-linux.zip"')
        os.system('chmod +x "./adb/platform-tools/adb"')
