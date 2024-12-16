import cv2 as cv


# resizing images and video frames (can be use3d for stanalone videos )
def resizeFrame(frame, scale=0.75):

    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimentions = (width, height)

    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

# changing resolution of a live capturre video only
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

# image capture
imgcap = cv.imread("images/stana1.jpg")

cv.imshow("stana1", imgcap)

cv.waitKey(0)


# video capture
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    resized_frame = resizeFrame(frame)
    # changeRes(200, 200)

    cv.imshow("resized video", resized_frame)

    cv.imshow("Video", frame)
    # cv.waitKey(1)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()






