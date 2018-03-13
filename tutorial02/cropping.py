import cv2
import numpy as np
import os
import shutil

"""
Tutorial for crop image 
"""


img = cv2.imread('./images/lena.jpg')


row, col, ch = img.shape
patch_size = 50
stried = 5

patch_index = 0

# If the folder already exists, remove it and all of files inside.
if os.path.exists('./patched'):
    shutil.rmtree('./patched')

# Make new folder
os.mkdir('./patched/')

for i in range(0, row-patch_size+1, 30):
    for j in range(0, col-patch_size+1, 30):
        patch = img[i:i+patch_size-1, j:j+patch_size-1]
        filename = "patched/patch%05d.png" % patch_index
        cv2.imwrite(filename, patch)
        patch_index+=1
        print("[Done] %s" % filename)

