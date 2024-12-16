import cv2 as cv
import numpy as np
from myfunc import resizeFrame
from myfunc import putSize

# read image frame
img = cv.imread("images/stana3.jpg")
img = resizeFrame(img, .4)
img = putSize(img)
cv.imshow("img", img)


# blank image
blank = np.zeros((700,400, 3), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (100, 200), (300, 500), (0,122,255), thickness=-1)
cv.imshow("rec", rectangle)

circle = cv.circle(blank.copy(), (50,350), 90, (200,0,120), thickness=-1)
cv.imshow("circle", circle)

# bitwise and 
bitwiseAnd = cv.bitwise_and(rectangle, circle)
cv.imshow("and", bitwiseAnd)

# bitwise or 
bitwiseOr = cv.bitwise_or(rectangle, circle)
cv.imshow("or", bitwiseOr)

# bitwise xor (returns non intersecting areas)
bitwiseXor = cv.bitwise_xor(rectangle, circle)
cv.imshow("xor", bitwiseXor)

# bitwise not 
bitwiseNot = cv.bitwise_not( circle)
cv.imshow("not", bitwiseNot)



cv.waitKey(0)