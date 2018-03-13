# Using External Libraries


1. Scikit-Image library
    - http://scikit-image.org/docs/dev/api/skimage.filters.html
    - provides many filters, utility, ... etc
```python
import cv2
import numpy as np
import skimage 
from skimage import filters, io

img = cv2.imread('./images/lena.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

res = filters.sobel(gray)
#.......

```


