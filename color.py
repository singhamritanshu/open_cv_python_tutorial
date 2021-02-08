import cv2 as cv

img = cv.imread("test_images/kohli_1.jpg")

# BGR to gray scale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("Gray",gray)

# BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
#cv.imshow("HSV",hsv)

# BGR to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
#cv.imshow("LSB",lab)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
#cv.imshow("RGB",rgb)
