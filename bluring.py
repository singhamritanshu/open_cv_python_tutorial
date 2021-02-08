import cv2 as cv
img = cv.imread("test_images/boston.png")

cv.imshow("Original",img)

# Averaging: Value of center pixel is the average of it's surrounding pixel
average =  cv.blur(img,(5,5))
cv.imshow("Average",average)

# Gaussian blur: Each surrounding pixel is give a particular weight and the center value of the kernel window is the average of the products of thoes weights
gau_blur = cv.GaussianBlur(img,(5,5),0) # sigma_x is the s.d along the x-axis
cv.imshow("Gaussian", gau_blur)

# Median blur: Value of the center pixel is the median of the surrounding pixel. It is bit more effective in reduceing the noise inthe picture tahn the other two methods we have disscussed. It is used with kernel size of 3 mostly to reduce the noise in the image.
median = cv.medianBlur(img,5) 
cv.imshow("Median", median)

# Bilateral blur: It applies blurring but retains the edges in the image.
# Sigma space: It basically determines how far the pixel values outside the kernel window will be used for calculating the central pixel value.
bilat = cv.bilateralFilter(img,5,15,15)
cv.imshow("Bilateral",bilat)

cv.waitKey(0)