import os

# author: Abhishek Rana, Web programmer
# website: https://www.quora.com/How-do-I-close-my-web-browser-using-python

# Windows
browserExe = "chrome.exe"
os.system("taskkill /f /im " + browserExe)
# đóng tất cả cửa sổ chrome

# If you are using Linux
# import os
# browserExe = "chrome"
# os.system("pkill "+browserExe)
