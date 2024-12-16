import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from myfunc import resizeFrame
from myfunc import putSize



# read image frame
img = cv.imread("images/stana2.jpg")
img = resizeFrame(img, .4)
img = putSize(img)
# cv.imshow("img", img)


# plt.imshow(img)
# plt.show()


# bgr to grey scale

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grey", grey)

# bgr to hsv

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("hsv", hsv)

# bgr to lab

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow("lab", lab)

# bgr to rgb

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow("rgb", rgb)

# grey scale to bgr

bgr = cv.cvtColor(grey, cv.COLOR_GRAY2BGR)
cv.imshow("bgr", bgr)


cv.waitKey(0)
