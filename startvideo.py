# from pyautogui import *
import pyautogui
import time
import random
for s in range(1,8):
    print(s)
    print('apakah sudah muter')
    time.sleep(1)
    pyautogui.moveTo(283, 283)
    print(s)
    pyautogui.moveTo(476, 354)
    time.sleep(1)
    print(s)
    pyautogui.moveTo(236, 336)
    time.sleep(1)
    
    
    if pyautogui.locateCenterOnScreen('startvideo.png', confidence=0.9) !=None:
        x, y = pyautogui.locateCenterOnScreen('startvideo.png', confidence=0.9)
        time.sleep(1)
        pyautogui.click(x, y)
        print('video belum muter')
        random_name = (random.randint(100,102))
        screenshot = pyautogui.screenshot()
        save_path = "{}screenshot.png".format(random_name)
        screenshot.save(save_path)
        print('wait loading image')
        exit(0)
      

    
