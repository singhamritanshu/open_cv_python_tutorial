import cv2 as cv

img = cv.imread("test_images/kohli_1.jpg")
cv.imshow("Image",img)

# Converting an image to greyscale 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#Blur an image 
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT) # To increase the blur increase the kernel size keep it odd.
cv.imshow("Blur",blur)

# Canny Edge Cascade
canny = cv.Canny(img,125,175) # you can reduce the amount of edegs foud by applying the blur
cv.imshow("Canny",canny)

# Dilating an images
dilated = cv.dilate(canny,(5,5),iterations=3)
cv.imshow("Dilated",dilated)

# Eroding an images
erroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow("Eroded",erroded)

# Resize an image
resized = cv.resize(img,(500,500), interpolation=cv.INTER_LINEAR) # We can also use INTER_CUBIC,_LINEAR,_AREA
cv.imshow("Resized",resized)

# Cropping an image. Cropping works by slicing the array as images are represented as image.
cropped = img[100:150,200:300]
cv.imshow("cropped",cropped)

cv.waitKey(0)
