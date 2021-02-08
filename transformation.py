import cv2 as cv
import numpy as np 

img = cv.imread("test_images/kohli_1.jpg")

# Translation: Shifting an image along x & y axis.

def translate(img, x, y):
    trans_mat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,trans_mat,dimension)

# x: Shift right
# -x: Shift left
# y: Shift down
# -y: Shift up

trans = translate(img,100,-100)
cv.imshow("Translated", trans)

# Rotating an image 

def rotate(img,angle,rot_point=None):
    (height,width)=(img.shape[1],img.shape[0])
    if rot_point is None:
        rot_point = (height//2,width//2) # If rotation point is not provided then we rotate the image from the center 
    rot_mat = cv.getRotationMatrix2D(rot_point,angle,1.0)
    dimension = (height,width)

    return cv.warpAffine(img,rot_mat,dimension)

rotated = rotate(img,45)
cv.imshow("Rotated",rotated)

# Flipping an Image
# flip_code can be:
# 0: Flipping the image vertically
# 1: Flipping the image horizontally
# -1: Flipping the image both vertically and horizontally

flipped = cv.flip(img,0) 
cv.imshow("Flipped", flipped)


cv.waitKey(0)
