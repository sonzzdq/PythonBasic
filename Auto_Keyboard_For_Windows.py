from pyautogui import press, typewrite, keyDown, keyUp
import time


# mục đích code: dùng để tự động một số thao tác lặp đi lặp lại

def Tu_Dong_Go_Phim():
    time.sleep(2)
    i = 0
    while i < 10:
        i += 1
        keyDown('enter', pause=0.25)
        keyUp('enter', pause=0.25)
        typewrite(str(i), interval=0.5)
        # keyDown('left', pause=0.25)
        # keyUp('left', pause=0.25)
        # typewrite(str(i), interval=0.5)
        # keyDown('right', pause=0.25)
        # keyUp('right', pause=0.25)
        # keyDown('down', pause=0.25)
        # keyUp('down', pause=0.25)
