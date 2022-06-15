from pyautogui import *
import pyautogui
import time

for s in range(1,20):
    print(s)
    time.sleep(1)
    if pyautogui.locateCenterOnScreen('1.png', confidence=0.9) !=None:
        x, y = pyautogui.locateCenterOnScreen('1.png', confidence=0.9)
        time.sleep(3)
        pyautogui.click(x, y)
    
    else:
        print('wait for image')
        time.sleep(1)
    if pyautogui.locateCenterOnScreen('2.png', confidence=0.9) !=None:
        x, y = pyautogui.locateCenterOnScreen('2.png', confidence=0.9)
        time.sleep(1)
        pyautogui.click(x, y)
    else:
        print('wait for image')
        time.sleep(1)
    if pyautogui.locateCenterOnScreen('3.png', confidence=0.9) !=None:
        print('steps done')
        exit(0)
    else:
        print('wait for image')
        time.sleep(1)
