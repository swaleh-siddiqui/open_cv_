import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 
from myfunc import resizeFrame
from myfunc import putSize

# read image frame
img = cv.imread("cats/cat1.jpg")
img = resizeFrame(img, .4)
img = putSize(img)
cv.imshow("img", img)

# simple thresholding

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grey", grey)

threshold, thresh = cv.threshold(grey, 150, 255, cv.THRESH_BINARY)
# cv.imshow("thresh", thresh)

# inverse thresholding

threshold_i, thresh_inverse = cv.threshold(grey, 150, 255, cv.THRESH_BINARY_INV)
# cv.imshow("thresh_inverse", thresh_inverse)


# adaptive thresholding

adapt = cv.adaptiveThreshold(grey, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("adapt", adapt)


cv.waitKey(0)