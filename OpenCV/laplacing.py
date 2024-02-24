import cv2 as cv
import numpy as np


img = cv.VideoCapture(0)

while True:
    ret,frame = img.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    laplace = cv.Laplacian(gray, cv.CV_64F, )
    laplace = np.int8(np.absolute(laplace))
    canny = cv.Canny(gray, 150,175)
    cv.imshow('canny', canny)
    cv.imshow('webcam', laplace)
    if cv.waitKey(1)&0xFF == ord('q'):
        break


img.release()
cv.destroyAllWindows()
