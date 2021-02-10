import cv2 as cv 
import numpy as np 

img = cv.imread("test_images/boston.png")
cv.imshow("Original",img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Canny
canny = cv.Canny(gray,155,255)
cv.imshow("Canny",canny)
# Laplacian
lap = cv.Laplacian(gray,cv.CV_64F) # CV_64F is the datadepth(ddepth) value.
lap = np.uint8(np.absolute(lap))# Image pixel cannot have a negative value so we calculate absolute value and then we convert it to image specific data type i.e. uint8.
cv.imshow("Laplacian",lap)

# Sobel: It computes the gradient in two direction i.e x & y.
sobel_x = cv.Sobel(gray,cv.CV_64F,1,0) # dx=1,dy=0
cv.imshow("Sobel X",sobel_x)
sobel_y = cv.Sobel(gray,cv.CV_64F,0,1)
cv.imshow("Sobel Y",sobel_y)
# Combining both sobel_x & sobel_y
combined_sobel = cv.bitwise_or(sobel_x,sobel_y)
cv.imshow("Combined Sobel", combined_sobel)

cv.waitKey(0)