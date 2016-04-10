import datetime
import sys
import time

import vd

time.sleep(3)
# pyautogui.click()    # click to put drawing program in focus
# distance = 0
# while distance < 100:
#     pyautogui.dragRel(distance, 0, duration=0.2)   # move right
#     distance = distance + 5
#     pyautogui.dragRel(0, distance, duration=0.2)   # move down
#     pyautogui.dragRel(-distance, 0, duration=0.2)  # move left
#     distance = distance + 5
#     pyautogui.dragRel(0, -distance, duration=0.2)  # move up
# ngày giờ hiện tại
NTime = datetime.datetime.now()
# định dạng theo yyyy/mm/dd hh:mm:ss
NTime = (NTime.strftime("%Y/%m/%d %H:%M:%S"))
print(NTime)
f = open('E:\Downloads\demo_file2.txt', 'w')
f.write(NTime)
time.sleep(3)
vd.main()
