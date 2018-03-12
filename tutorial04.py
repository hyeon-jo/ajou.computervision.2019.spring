import cv2
import numpy as np
from skimage import filters, io
import matplotlib.pyplot as plt


img = cv2.imread('./images/lena.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# res = filters.sobel(gray)
res = filters.gaussian(gray)


# plt.imshow(cv2.cvtColor(res, cv2.COLOR_RGB2BGR))??
plt.imshow(res, cmap='gray')
plt.show()

