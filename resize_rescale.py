# This will work for images, video, live videos
import cv2 as cv
def rescale_frame(frame, scale_value=0.35):
    height = int(frame.shape[0] * scale_value) # frame.shape[1] this contains the height of the frame 
    width = int(frame.shape[1] * scale_value)  # frame.shape[0] this contains the width of the frame
    dimensions = (width,height)
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# This will work only for live videos 
def rescale_frame_vid(width, height):
    capture = cv.VideoCapture(0)
    capture.set(3,width)
    capture.set(4,height)
    
