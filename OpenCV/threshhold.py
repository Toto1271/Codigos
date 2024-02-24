import cv2 as cv
import numpy as np


img = cv.VideoCapture(0)

while True:
    ret,frame = img.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    threshold, thresh = cv.threshold(gray, 120, 255,cv.THRESH_BINARY)
    cv.imshow('webcam', thresh)
    if cv.waitKey(1)&0xFF == ord('q'):
        break


img.release()
cv.destroyAllWindows()
