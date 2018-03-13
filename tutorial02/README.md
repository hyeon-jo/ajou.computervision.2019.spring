# Access and Operation to Pixel


1. Access to Pixel
```python
import cv2
import numpy as np
img = cv2.imread('./images/lena.jpg')

row = 17
col = 30

# In RGB, BGR, HSV images, each pixel is a list of channels
pixel_value = img[row][col]
print(pixel_value)

# In gray scale images, each pixel has one value (intensity)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
pixel_value = gray[row][col]
print(pixel_value)

```


2. Access to Range
```python
import cv2
import numpy as np
img = cv2.imread('./images/lena.jpg')

row = 17 
height = 20
col = 30
width = 30

img2 = img[row:row+height-1, col:col+width-1]

cv2.imshow(img2)
cv2.waitKey(0)
```