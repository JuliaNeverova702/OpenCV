from PIL import Image, ImageEnhance 
import cv2
from os import mkdir, rmdir, listdir, rename
import numpy as np


def main():    
    path_to_source_data = "../JPEGImagesOld/"
    path_to_res         = "../JPEGImages/"


    rename("../JPEGImages/", path_to_source_data)
    create_res_dir(path_to_res)
    improve(path_to_source_data, path_to_res)

    
def get_brightness(path_to_source_data):
    tsize = 256
    image = path_to_source_data + filename
    for filename in listdir(path_to_source_data):
        if ".jpg" in filename:
            brightness = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)[..., 0]
            


    return brightness

def create_res_dir(path_to_res):
    try:
        mkdir(path_to_res)
    except:
        print("Unable to create directory")


def improve(path_to_source_data, path_to_res):
    for filename in listdir(path_to_source_data):
        if ".jpg" in filename:
            image = Image.open(path_to_source_data + filename)
            sharpness = ImageEnhance.Sharpness(image)
            brightness = ImageEnhance.Brightness(image)

            factor_enh = 6
            factor_br = 2

            new_image = sharpness.enhance(factor_enh) 
            new_image = brightness.enhance(factor_br)  
            new_image.save(path_to_res + filename)


if __name__ == "__main__":
    main()
