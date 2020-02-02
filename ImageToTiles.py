# -*- coding: utf-8 -*-
"""
@author: archit
"""
"""
    ----------------------------------Author's Note---------------------------------------
    
    Image to Tiles is a advanced numpy resource which presents an example of how numpy functions 
    can help reduce writing unnecessary loops in python. The code contains use of numpy attributes like
    shape and strides. It also uses numpy functions like np.ravel and np.lib.stride_tricks.as_strided
    
    divmod is a python function which returns the quotient and remainder for divident and divisor as inputs.
    Usage of magic functions like %timeit can be used to compare the optimized and the unoptimized code.
    
    ---------------------------------------------------------------------------------------
"""
# Importing the necessary libraries
import numpy as np
import cv2 # Used for testing with an image
import matplotlib.pyplot as plt # Used for testing with an image


# The main function which makes a nxn image into an mxm tiles with default m is 8.
def get_tile_images(image, width=8, height=8):
    _nrows, _ncols, depth = image.shape
    _strides = image.strides
    
    # Handling the case for the tiles to be perfectly fit the original image. Cannot have incomplete tiles
    nrows, _m = divmod(_nrows, height) 
    ncols, _n = divmod(_ncols, width)
    if _m != 0 or _n != 0:
        return None
#    temp =(height * _strides[0], width * _strides[1], *_strides)
#    print (temp)

    return np.lib.stride_tricks.as_strided(
        np.ravel(image),
        shape=(nrows, ncols, height, width, depth),
        strides=(height * _strides[0], width * _strides[1], *_strides),
        writeable=False
    )
#Assume that we have a_image of shape (1080, 1928, 3). To get a 135x240 tiles (each small image has size 8x8):

"""
    Written below is a code for testing the above written code
    Can read image by any of cv2, matplotlib or scikit-learn
"""

path_to_image = ""
#image = plt.imread(a_image)
image = cv2.imread(path_to_image)
cv2.imshow("Test",image)
cv2.waitKey(0)
tiles = get_tile_images(image, 8, 8)

"""
    Written below is the code to avoid in order to become a better coder in python language
"""

_nrows = int(image.shape[0] / 16)
_ncols = int(image.shape[1] / 16)
#
temp = np.ones((1080,1920,3),dtype = np.uint8)
#
for i in range(0,np.size(tiles,axis=0)):
    for j in range(0,np.size(tiles,axis=1)):
        temp[i * 8:i * 8 + 8,j * 8:j * 8 + 8] = tiles[i,j,:,:,:]    
        

cv2.imshow("Test",temp)
cv2.waitKey(0)

#fig, ax = plt.subplots(nrows=_nrows, ncols=_ncols)
#
#for i in range(_nrows):
#    for j in range(_ncols):
#        ax[i, j].imshow(tiles[i, j]); ax[i, j].set_axis_off();
