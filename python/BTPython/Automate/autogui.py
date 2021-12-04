#import pyautogui

"""
screenWidth, screenHeight = pyautogui.size()
#pyautogui.moveTo(100, 100)
pyautogui.write('Hello world!', interval=0.25)
pyautogui.press('esc') 
#print(screenWidth, screenHeight)
"""

"""
pyautogui.moveTo(125, 267)
distance = 50
while distance > 0:
        pyautogui.drag(distance, 0, duration=0.5)   # move right
        distance -= 5
        pyautogui.drag(0, distance, duration=0.5)   # move down
        pyautogui.drag(0, 0, duration=0.5)  # move left
        distance -= 5
        pyautogui.drag(0, 0, duration=0.5)  # move up
        if pyautogui.hotkey('esc'):
            break
        """
#! python3
#import datetime

import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')