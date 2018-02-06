import snap7
from snap7_lib import *
import sys
import os
import time

plc = S71200('192.168.1.61') 

status_ant = 0
While True:
    status = plc.getMem('ix1.1')   
    print(status)
    if status != status_ant:
        text = "ON"
        if status == 0:
            text = "OFF"
        os.exec("python telegram.py" +text )
    status_ant = status
    time.sleep(2)

plc.disconnect()
