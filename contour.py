import cv2 as cv 
import numpy as np 
# Contours: Contours are basically the boundries of objects, the line or the curve that joins the objects.

img = cv.imread("test_images/boston.png")
blank = np.zeros(img.shape, dtype= 'uint8') # Creating a blank image of the same size to draw contours


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
canny = cv.Canny(gray,125,175) # We use blur insted gray to reduce the number of countours.
# We detect contours by using find contur method, this return two things contours and hirarchies

# Different types of hirarchies modes: 
# 1) cv.RETR_TREE: If you want all the hierarchical contours.
# 2) cv.RETR_EXTERNAL: If you want only the external contours.
# 3) cv.RETR_LIST: If you want all the contours in an image.

# This function findCountours collects all the countours (co-ordinates of the countours) from the edges and stores them in list and it also returns the their hierarchie.
# RETR_LIST is the mode in which the function finds the countours
# cv.CHAIN_APPROX_NONE is how we want to aprroximate the countours. 
# CHAIN_APPROX_NONE: It does nothing it simplly returns the countours
#CHAIN_APPROX_SIMPLE: It simplly compresse all the countours and returns(In cas of a line none will return all the points wehere as simple will compress all the points and return the end co-ordinates).

# Insted of using canny to find contours we can also use threshold.
# Threshold basically takes the image and binarize it 
ret, thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY) # What it does is that all the pixel values which are less than 125 (threshold value) is set to 0 which is black where as all the pixel values greater than 125(threshold value) is set to 255 white.

countours_1, hierarchies_1 = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE) # Finding contours using canny 
countours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)# Finding contours using threshold

print(f'{len(countours)} countours(s) found using threshold method')
print(f'{len(countours_1)} countours found using canny edge detection')
cv.imshow("Threshold", thresh)

# Drawing the countours on the blank image 
cv.drawContours(blank,countours,-1,(255,255,255),1)
cv.imshow("Threshold Countours", blank)

# Painting the image black again
blank[:]=0,0,0
cv.drawContours(blank,countours_1,-1,(255,255,255),1)
cv.imshow("Canny Contour", blank)

cv.imshow("Original",img)
cv.waitKey(0)