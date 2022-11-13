import cv2
import numpy as np

import os

path = "JPEGImages/"

for filename in os.listdir(path):
    if ".jpg" in filename:
        image = cv2.imread(path + filename)
        height, width, channels = image.shape
        resultimage = np.zeros((height, width))

        image_norm = cv2.normalize(image, resultimage, alpha=0,beta=200, norm_type=cv2.NORM_MINMAX)
        isWritten = cv2.imwrite(f"JPEGnew/{filename}", image_norm)
