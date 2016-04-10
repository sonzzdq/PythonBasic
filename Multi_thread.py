import threading
import win32api
import sys
from pyautogui import press, typewrite, keyDown, keyUp
import time
import queue


# mục đích code: dùng để tự động một số thao tác lặp đi lặp lại

def Tu_Dong_Go_Phim():
    time.sleep(2)
    i = 0
    while i < 10:
        i += 1
        keyDown('enter', pause=0.25)
        keyUp('enter', pause=0.25)
        typewrite(str(i), interval=0.5)


def toa_do_mouse():
    while True:
        h_x, h_y = win32api.GetCursorPos()
        if h_x == 0:
            tudong._is_stopped = True  # <--- no hoat dong
            SystemExit  # <--- hoat dong
            print("thoat chuong trinh")
            e = 2 / 0
            sys.exit()
            # # bị lỗi nhưng ít ra cũng dừng lại

            # sys.exit()

        # elif win32api.GetAsyncKeyState(ord('H')) == True:
        #     sys.exit()
        time.sleep(1)
        print(str(h_x) + ' ' + str(h_y))


# w2 = threading.Thread(target=toa_do_mouse) # use default name
tudong = threading.Thread(name='Tu_Dong_Go_Phim', target=Tu_Dong_Go_Phim)
toado = threading.Thread(name='toa_do_mouse', target=toa_do_mouse)


def gogo():
    tudong.Daemon = True
    toado.start()
    # w2.start()
    tudong.start()


if __name__ == '__main__':
    gogo()

# tt


1
2
3
4
5
