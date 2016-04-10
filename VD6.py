import win32api
import time
import sys


def msa():
    while True:
        h_x, h_y = win32api.GetCursorPos()
        if h_x == 0:
            sys.exit()
        # elif win32api.GetAsyncKeyState(ord('H')) == True:
        #     sys.exit()
        time.sleep(1)
        print(str(h_x) + ' ' + str(h_y))
