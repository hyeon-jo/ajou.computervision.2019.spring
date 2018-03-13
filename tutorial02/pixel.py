import cv2
import numpy as np
img = cv2.imread('./images/lena.jpg')

row = 17
col = 30

pixel_value = img[row][col]
print(pixel_value)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
pixel_value = gray[row][col]
print(pixel_value)
