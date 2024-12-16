import cv2 as cv
import numpy as np
from myfunc import resizeFrame
from myfunc import putSize

# read image frame
img = cv.imread("images/stana1.jpg")
img = resizeFrame(img, .4)
img = putSize(img)
cv.imshow("img", img)


# splitting the bgr color channels
b, g, r = cv.split(img)
# cv.imshow("blue", b)
# cv.imshow("green", g)
# cv.imshow("red", r)

blank = np.zeros((img.shape[:2]), dtype="uint8")
blue = cv.merge([b,blank, blank])
cv.imshow("blue", blue)
green = cv.merge([blank, g, blank])
cv.imshow("green", green)
red = cv.merge([blank, blank, r])
cv.imshow("red", red)


# merge color channels
merged = cv.merge([b,g,r])
# cv.imshow("merged", merged)

cv.waitKey(0)