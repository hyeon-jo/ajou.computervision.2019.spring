import cv2
import matplotlib.pyplot as plt
import numpy as np


"""
Change the color space of image using 'cvtColor()'
OpenCV use RGB space as the default space
"""

img = cv2.imread('./images/lena.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imwrite('output.png', gray)
cv2.imshow('gray image', gray)
cv2.waitKey()

print("done")

