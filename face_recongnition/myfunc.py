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