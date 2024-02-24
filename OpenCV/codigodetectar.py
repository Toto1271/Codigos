import cv2 as cv
import numpy as np
import time


farm = cv.imread('farm.png',cv.IMREAD_UNCHANGED)
needle = cv.imread('needle.png',cv.IMREAD_UNCHANGED)


cv.imshow('original', farm)
resultado = cv.matchTemplate(farm,needle, cv.TM_CCOEFF_NORMED)
cv.imshow('resultado', resultado)
minval,maxval,minloc,maxloc = cv.minMaxLoc(resultado)
w = needle.shape[1]
h = needle.shape[0]
cv.rectangle(farm, maxloc, (maxloc[0] + w, maxloc[1] + h), (0,255,255), 2)
cv.imshow('needle showed', farm)

cv.waitKey(0)
cv.destroyAllWindows()