# Bitwise operator operate in a binary manner. Mostly used in masking.
# AND, OR, XOR & Not

import cv2 as cv
import numpy as np 

blank = np.zeros((400,400),dtype='uint8')

rect = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
cir = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow("Recatangle",rect)
cv.imshow("Circle", cir)

# Bitwise AND: It returns the intersection of the two images.

bitwise_and = cv.bitwise_and(rect,cir)
cv.imshow("Bitwise_AND",bitwise_and)

# Bitwise OR: It returns the union of the two images.

bitwise_or = cv.bitwise_or(rect,cir)
cv.imshow("Bitwise_OR",bitwise_or)

# Bitwise XOR : It returns the non itersecting region.
bitwise_xor = cv.bitwise_xor(rect,cir)
cv.imshow("Bitwise_XOR",bitwise_xor)

# Bitwise Not: It inverts the binary color.
bitwise_not = cv.bitwise_not(cir)
cv.imshow("Bitwise_NOT_Cir",bitwise_not)

bitwise_not = cv.bitwise_not(rect)
cv.imshow("Bitwise_NOT_Rect",bitwise_not)

cv.waitKey(0)