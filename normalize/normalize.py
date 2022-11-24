import cv2
from os import mkdir, rmdir, listdir, rename
import numpy as np


def main():    
    path_to_source_data = "../JPEGImagesOld/"
    path_to_res         = "../JPEGImages/"

    rename("../JPEGImages/", path_to_source_data)
    create_res_dir(path_to_res)
    normalize(path_to_source_data, path_to_res)


def create_res_dir(path_to_res):
    try:
        mkdir(path_to_res)
    except:
        print("Unable to create directory")


def normalize(path_to_source_data, path_to_res):
    for filename in listdir(path_to_source_data):
        if ".jpg" in filename:  
            image = cv2.imread(path_to_source_data + filename)
            height, width, channels = image.shape
            resultimage = np.zeros((height, width))
            image_norm = cv2.normalize(image, resultimage, alpha=0,beta=200, norm_type=cv2.NORM_INF)
            save_result(path_to_res, filename, image_norm)


def save_result(path_to_res, filename, image_norm):
    try:
        cv2.imwrite(f"{path_to_res}{filename}", image_norm)
    except:
        print(f"{filename} not saved")


if __name__ == "__main__":
    main()


# norm_type:

# NORM_INF
# NORM_L1
# NORM_L2
# NORM_L2SQR
# NORM_HAMMING
# NORM_HAMMING2
# NORM_TYPE_MASK
# NORM_RELATIVE
# NORM_MINMAX