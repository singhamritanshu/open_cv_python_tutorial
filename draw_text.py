import cv2 as cv
import numpy as np

# Creating a blank image
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow("blank", blank)

# Paint the image of a certain color

blank[:]=0,0,255 # Painting red color
cv.imshow("Red",blank)

blank[:]=255,0,0 # Painting blue color
cv.imshow("Blue",blank)

blank[:]=0,255,0 # Painting green color
cv.imshow("Green",blank)

#Painting the image black again
blank[:]=0,0,0 

# Painting a certain portion of the image green 
blank[200:300,300:400]=0,255,0
cv.imshow("Portion",blank)

# Drawing a rectangle 
cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=3)
cv.imshow("Rectangle",blank)

# If you want to fill the entire rectangle by a certain color
cv.rectangle(blank,(0,0),(250,500),(0,0,255),thickness=cv.FILLED) # You can also just use -1 in place thickness to get the filled image(thickness=-1).
cv.imshow("Filled", blank)
 
blank[:]=0,0,0
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,255),thickness=-1)
cv.imshow("Filled2",blank)

# Drawing a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),50,(0,255,0), thickness=3)
cv.imshow("Circle",blank)

#Draw a line
cv.line(blank,(0,0),(250,250),(255,255,255),thickness=3)
cv.imshow("Line",blank)

# Write a text on an image
cv.putText(blank,"Hello I'm Amritanshu",(0,225),cv.FONT_HERSHEY_DUPLEX,1.0,(255,255,255),thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)