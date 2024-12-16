import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 
from myfunc import resizeFrame
from myfunc import putSize

# read image frame
img = cv.imread("cats/cat1.jpg")
img = resizeFrame(img, .4)
img = putSize(img)
# cv.imshow("img", img)


# grey scale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grey", grey)


# laplacian method

lap = cv.Laplacian(grey, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
# cv.imshow("lpa", lap)

# solbel

sobel_x = cv.Sobel(grey, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(grey, cv.CV_64F, 0, 1)
cv.imshow("sobelx", sobel_x)
cv.imshow("sobely", sobel_y)

combined = cv.bitwise_or(sobel_x, sobel_y)
cv.imshow("combined", combined)

cv.waitKey(0)