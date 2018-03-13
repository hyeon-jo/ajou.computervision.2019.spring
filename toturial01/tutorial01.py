import cv2
import numpy as np

"""
Load image from file using cv2 
[cv2.imagead] function load image from file and save into your variable with np.ndarray type
"""

img = cv2.imread("./images/lena.jpg")

# you can assert after imread() like below
assert type(img) == np.ndarray, "Failed to read image"

cv2.imshow('my image', img)
cv2.waitKey(0)
