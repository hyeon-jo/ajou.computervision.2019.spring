# Image Read and Write with cv2 lib

Almost libraries in python use numpy array. cv2 library provide us basic I/O and Converting methods. 

1. Importing Libraries
```python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
``` 

2. Load image from file 
```python
img = cv2.imread('path/filename')

assert type(img)==np.ndarray, "Failed to load image"

print(img.shape)
```

3. Save image into file
```python
cv2.imwrite('path/filename')
```

4. Show image on pop up and wait to my keyboard input
```python
img = cv2.imread('path/filename') #any image data in numpy array type
cv2.imshow('popup_title', img)
cv2.waitkey(0)
```

5. Change the color space of image
```python
img = cv2.imread('path/filename', cv2.IMREAD_COLOR) #any image data 

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow('popup_title', img)
cv2.waitkey(0)
``` 
