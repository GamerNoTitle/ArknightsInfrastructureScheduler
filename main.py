import os

# from utils.adb import 
from utils.Initalize import Initalize
from utils.ProgressBar import download

if __name__ == '__main__':
    if not os.path.exists('./adb'): 
        Initalize()