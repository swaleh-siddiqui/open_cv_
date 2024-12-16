import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 
from myfunc import resizeFrame
from myfunc import putSize

# read image frame
img = cv.imread("images/stana1.jpg")
img = resizeFrame(img, .4)
img = putSize(img)
cv.imshow("img", img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grey", grey)

# grey histogram
grey_hist = cv.calcHist([grey], [0], None, [256], [0,256])

plt.figure()
plt.title("color histogram")
plt.xlabel("Bins")
plt.ylabel("no. of pixwls")
# plt.plot(grey_hist)
# plt.xlim([0,256])
# plt.show()


# colour histogram

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    
plt.show()

cv.waitKey(0)