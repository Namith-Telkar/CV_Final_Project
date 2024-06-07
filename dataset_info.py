#Code to check the image size and unique pixel values in the image masks
import cv2
import os
import numpy as np


# Path to the images folder
path = 'data/images/'

# Loop through the images in the folder
for img in os.listdir(path):
    img = cv2.imread(os.path.join(path, img))
    img_size = img.shape
    print('THE IMAGE SIZE: ',img_size)
    break

# Path to the image folder
path = 'data/masks/'

# Loop through the masks in the folder
for img in os.listdir(path):
    # Read the image
    img = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
    # Get the unique pixel values
    unique_pixel = np.unique(img)
    print(f'THE UNIQUE PIXEL VALUES IN IMAGE: {unique_pixel} AND THE NUMBER OF UNIQUE PIXELS: {len(unique_pixel)}')
    break