#Launch Game Before Running

import time
import pyautogui

while (True):
    currentMouseX, currentMouseY = pyautogui.position()
    print(currentMouseX, currentMouseY)
    time.sleep(5)