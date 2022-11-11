import cv2
import numpy as np

import os
 
for filename in os.listdir('/JPEGImages'):
        if filename[filename.rfind(".") + 1:] in ['jpg']:
            image = cv2.imread("*.jpg")
            image_norm = cv2.normalize(image, None, alpha=0,beta=200, norm_type=cv2.NORM_MINMAX)

cv2.imshow('original Image', image)
cv2.imshow('Normalized Image', image_norm)
cv2.waitKey(0)
cv2.destroyAllWindows()