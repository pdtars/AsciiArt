# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 20:44:40 2019

@author: Paulo
"""

from PIL import Image
import numpy as np

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# 10 levels of gray
gscale2 = "@%#*+=-:. "

image = Image.open("FB_20150331_00_52_01_Saved_Picture.jpg").convert("L")


W,H = image.size[0],image.size[1]

im = np.array(image)

w,h = im.shape
greyavg = np.average(im.reshape(w*h))


#image.show()