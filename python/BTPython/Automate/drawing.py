import sys
import cv2
import time
import random
import pyautogui as pg

print('Press Ctrl-C to quit.')
"""
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
    """

# open source image
originalImage = cv2.imread('unnamed.jpg')

# convert image to grayscale
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)

# convert image to black and white
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

# uncomment below lines to preview image
cv2.imshow('Black & white image', blackAndWhiteImage)  
cv2.waitKey(0)
cv2.destroyAllWindows()

# global coordinates of where to start drawing (change if needed!)
x_start = 125
y_start = 267

# wait before user clicks on window to within
time.sleep(5)

# put mouse mointer into initial position
pg.moveTo(x_start, y_start)

# loop over pixel rows
for y in range(len(blackAndWhiteImage)):
    # init row
    row = blackAndWhiteImage[y]
    
    # loop over pixel cols
    for x in range(len(row)):
        if row[x] == 0:
            # draw pixel!
            pg.click(x_start + x, y_start + y, _pause=False)
            print('Drawing at:', x_start + x, y_start + y)
            
            # animation speed
            time.sleep(0.008)