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
img = cv.imread("images/nina7.jpg")
img = resizeFrame(img, .4)
img = putSize(img)
cv.imshow("img", img)


# translation of image frame
def translate(frame, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimentions = (frame.shape[1], frame.shape[0])
    return cv.warpAffine(frame, transMat, dimentions)

translated = translate(img, 100, 100)
# cv.imshow("translated", translated)


# rotation of the image frame
def rotate(frame, angle, centreOfRotation=None):
    (height, width) = (frame.shape[0], frame.shape[1])
    if (centreOfRotation == None):
        centreOfRotation = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(centreOfRotation, angle, 1.0)  # centre point, angle , zoom
    dimentions = (width, height)
    return cv.warpAffine(frame, rotMat, dimentions)

rotated = rotate(img, 45)
# cv.imshow("rotated", rotated)


# flipping the frame

flipped = cv.flip(img, 1)
cv.imshow("flipped", flipped)


cv.waitKey(0)