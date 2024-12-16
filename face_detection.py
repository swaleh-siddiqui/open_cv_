import cv2 as cv
import numpy as np
import matplotlib.pylab as lpt
from myfunc import resizeFrame
from myfunc import putSize

# read image
img = cv.imread("cats/cat1.jpg")
img = resizeFrame(img, .4)
img = putSize(img)
# cv.imshow("img", img)

# grey
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("grey", grey)

# impoting harr_cascade face detection file in a variable
harr_cascade = cv.CascadeClassifier("models/harr_face.xml")


# thix will return a list of rectangular coordinates of the box inside which the face is
face_rect = harr_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=3)
# fece_rect has the touple as it is (upper_left_corner_x, upper_left_corner_y, width, height)

print("number of faces in the image detected is " + str(len(face_rect)))


# now drawing the recatngle over the original image 
for (x, y, w, h) in face_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)


# cv.imshow("face_detected", img)



# live video face detection 

capture = cv.VideoCapture(0)

while True:

    isTrue, frame = capture.read()

    # frame_grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_mat = harr_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=3)

    for (x, y, w, h) in face_mat:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), thickness=2)

    cv.imshow("video", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)