# from pyautogui import *
import pyautogui
import time
import random
while 1:
    print('wait loading image')
    time.sleep(1)
    if pyautogui.locateCenterOnScreen('startvideo.png', confidence=0.9) !=None:
        x, y = pyautogui.locateCenterOnScreen('startvideo.png', confidence=0.9)
        time.sleep(1)
        pyautogui.click(x, y)
        print('steps done')
        exit(0)

    
