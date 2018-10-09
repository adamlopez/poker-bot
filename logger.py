import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import logging
import datetime as dt

def getLogger():
    textLogger = logging.getLogger('logs/')
    textLogger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

    file = f'{textLogger.name}/{dt.datetime.now().date()}.log' if os.path.isdir(textLogger.name) else f'{dt.datetime.now().date()}.log'
    fh = logging.FileHandler(file)
    fh.setLevel(logging.DEBUG) #file stores everything logged
    fh.setFormatter(formatter)
    textLogger.addHandler(fh)

    ch = logging.StreamHandler() #lets you print to display while logging
    ch.setLevel(logging.WARNING) # everything other than debug level msgs will be displayed on console
    ch.setFormatter(formatter)
    textLogger.addHandler(ch)
    return textLogger
