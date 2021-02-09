import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("test_images/kohli_1.jpg")
cv.imshow("Original", img)

# Calculating histogram for gray image 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) 
#cv.imshow("Gray",gray) 

# Creating mask 
blank = np.zeros(img.shape[:2],dtype="uint8")
mask = cv.circle(blank,(img.shape[1]//2-40,img.shape[0]//2-200),160,255,-1)
mask_gray = cv.bitwise_and(gray,gray,mask=mask)
#cv.imshow("Masked Image",mask_gray)

gray_hist = cv.calcHist([gray], [0], mask_gray, [256], [0,256] )


plt.figure()
plt.title("Histogram for gray masked face")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])

# Cumputing histogram for color image 
color = ('b','g','r')
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow("Masked Image",masked)
plt.figure()
plt.title("Histogram for color image")
plt.xlabel("bins")
plt.ylabel("number of pixels")
 
for i, j in enumerate(color):
    clo_his = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(clo_his,color=j)
    plt.xlim(0,256)
plt.show()

cv.waitKey(0)