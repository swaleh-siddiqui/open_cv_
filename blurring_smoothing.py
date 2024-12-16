import cv2 as cv
import numpy as np
from myfunc import resizeFrame
from myfunc import putSize

# read image frame
img = cv.imread("images/stana3.jpg")
img = resizeFrame(img, .4)
img = putSize(img)
cv.imshow("img", img)


# average blurring (takes average value of the pixels in kernels and asign it to the centre pixel)
average = cv.blur(img , (1001,1))   # kernel is width , height 
# cv.imshow("average",average)

# gausian blurring (same as average but the pixel values are assigned weights and then takes average)  this is more natural and less blurry than average
gausian = cv.GaussianBlur(img, (7,7), 0)  # the last zero value represents the sigma(x) that is the standered deviation in x direction
# cv.imshow("gausian", gausian)

# median blurring (same as average but instead of average it takes the median value of the pixels ) this is used to reduce noise in the image
median = cv.medianBlur(img, 7) # the value seven is used as kernel size it is just that it can only use sqaure kernel
# cv.imshow("median", median)

# bilateral blurring
bilateral = cv.bilateralFilter(img, 50, 55, 55)  # here function call gets img, diametre, sigma(colour), space-sigma
cv.imshow("bilateral", bilateral)


cv.waitKey(0)