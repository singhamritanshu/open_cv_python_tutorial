import cv2 as cv 
import numpy as np
img = cv.imread("test_images/boston.png")
cv.imshow("Original Image", img)
print(img.shape)

# Splitting the blue, green & red color channels
b,g,r = cv.split(img)

cv.imshow("Blue",b)
cv.imshow("Green",g)
cv.imshow("Red",r)

print(b.shape)
print(g.shape)
print(r.shape)

# Merging back all the three color channels
mer = cv.merge([b,g,r])
cv.imshow("Merged",mer)

# Showing the individual colors insted of grayscale images

blank = np.zeros(img.shape[:2],dtype='uint8')
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("Blue",blue,)
cv.imshow("green",green)
cv.imshow("red",red)

print("\n",blank.shape)
print(blue.shape)
print(green.shape)
print(red.shape)

cv.waitKey(0)
