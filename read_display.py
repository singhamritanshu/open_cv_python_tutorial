import cv2 as cv
from resize_rescale import * 

# Reading and displaying an image 

#img = cv.imread('test_images/kohli_1.jpg')
#cv.imshow("Best batsman",img)
#img2=rescale_frame(img) # Resizing the image
#cv.imshow("Batsman",img2)
   
# Reading and displaying the video 

capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_frame(frame) # Resizing the video 
    cv.imshow("Video", frame)
    cv.imshow('Video Resized',frame_resized) 
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.waitKey(0),cv.destroyAllWindows()


