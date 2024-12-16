import cv2 as cv

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
img = cv.imread("images/stana4.jpg")
img = resizeFrame(img, .4)
img = putSize(img)
cv.imshow("img", img)

# turning to grey scale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# grey = resizeFrame(grey, .4)
grey = putSize(grey)
# cv.imshow("grey scale", grey)


# blurring the image frame
blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
# blur = resizeFrame(blur, 2)
# cv.imshow("Blur", blur)


# finding edges present in the images frame (Edge cascade)
canny = cv.Canny(img, 125, 175)
# cv.imshow("canny", canny)

# dialate

# eroded to get back canny from dialate

# resize the image frame 
resized = cv.resize(img, (2000, 2000), interpolation=cv.INTER_CUBIC) # INTER_AREA is for reducing the size and INTER_CUBIC is solw but for good quality when increasing the size of frame
# cv.imshow("resized", resized)

# cropping the image frame
cropped = img[50:700, 200:600]    # this is img[Upper:lower, left:right]
# cv.imshow("cropped", cropped)


cv.waitKey(0)