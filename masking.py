import cv2 as cv
import numpy as np
from myfunc import resizeFrame
from myfunc import putSize

# read image frame
img = cv.imread("images/stana3.jpg")
img = resizeFrame(img, .4)
img = putSize(img)
cv.imshow("img", img)

# blank img
blank = np.zeros((img.shape[0], img.shape[1]), dtype="uint8")
mask = cv.circle(blank.copy(), (216, 768//4), 100,  255, thickness=-1)

cv.imshow("mask", mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("masked", masked)

cv.waitKey(0)