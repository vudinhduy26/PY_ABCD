# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 23:39:19 2021

@author: duy
"""

from PIL import Image
img = Image.open("sasuke.jpeg")

# If you want a greyscale image, simply convert it to the L (Luminance) mode:
new_img = img.convert('L')
new_img.show()

# Or save it to a file
# new_img.save('rick-morty-L.png')