import cv2 as cv

img = cv.imread("test_images/boston.png")
cv.imshow("Original", img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# Simple thresholding 
# What it does is that all the pixel values which are less than 150 (threshold value) is set to 0 which is black where as all the pixel values greater than 150(threshold value) is set to 255 white.
threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)  
cv.imshow("Simple Thresh",thresh)
# Creating an inverse thresholded image 
# All the pixel values which are less than 150 (threshold value) is set to 255 which is white where as all the pixel values greater than 150(threshold value) is set to 0 black.
threshold, thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow("Simple Inverse Thresholded",thresh_inv) 

# Adaptive thresholding: In this we let the computer find and decide the optimal thresholding value for us.
# We are using mean in type of thresholding to calculate the optimal threshlod value.
# 7 is the kernel size used by the opencv to calculat ethe mean and the 3 is the c value which will subtracted from the mean to fine tune our optimal threshold value 
adaptive_thresh_mean = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,13,7) 
cv.imshow("Adaptive threshol mean",adaptive_thresh_mean)
adaptive_thresh_inv_mean = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,13,7) 
cv.imshow("Adaptive thresh_inv mean",adaptive_thresh_inv_mean)

#Adaptive thresholding using gaussian meathod: Gaussian just added the weight around thoes pixel value and computed the mean across those pixels.
adaptive_thresh_gau = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,13,7)
cv.imshow("Adaptive Gaussian ",adaptive_thresh_gau)
adaptive_thresh_gau_inv = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,13,7)
cv.imshow("Adaptive Gaussian Inverse", adaptive_thresh_gau_inv)
cv.waitKey(0)