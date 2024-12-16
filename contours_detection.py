import cv2 as cv
import numpy as np

# resize image frames
def resizeFrame(frame, scale=0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    # height = 400
    # width = 500
    dimentions = (width, height)
    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

# put size of the image on the upper left corner
def putSize(frame):
    text = str(frame.shape[0]) + " X " + str(frame.shape[1])
    cv.putText(frame, text, (50,50), cv.FONT_HERSHEY_DUPLEX, 1.5, (0,0,255), thickness=2)
    return frame



# read image
img = cv.imread("images/stana3.jpg")
img = resizeFrame(img, .4)
img = putSize(img)
cv.imshow("img", img)


# contour detection steps

# 1 - convert to grey scale

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("grey", grey)

# 2 - cascading edges by canny
canny = cv.Canny(img, 125, 175)
# cv.imshow("canny", canny)

# 3 - find contour method
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print("number of contours found " + str(len(contours)))
print(hierarchies)

# visualizing contours

blank = np.zeros((img.shape[0], img.shape[1], 3), dtype="uint8")
# cv.imshow("blank", blank)

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("contours", blank)

cv.waitKey(0)