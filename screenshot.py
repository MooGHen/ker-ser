import pyautogui
import time
import random
screenshot = pyautogui.screenshot()
screenshot.save('sd.png')
yahhh = (random.randint(50,90))
for waktu in range(1, 100):
    print(waktu)
    time.sleep(1)
    
    if waktu == yahhh:
        print('end')
        screenshot = pyautogui.screenshot()
        screenshot.save('waktuend.png')
        exit(0)
