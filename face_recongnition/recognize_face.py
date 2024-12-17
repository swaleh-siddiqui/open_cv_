import cv2 as cv
import numpy as np
import os

from myfunc import resizeFrame 

# getting the haar_cascade file in na variable
haar_cascade = cv.CascadeClassifier("../models/harr_face.xml")

# # loading features and labels 
# features = np.load("features.npy")
# labels = np.load("labels.npy")

# reading the trained model yml file
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

# now create the mapping for the people
people = []
for i in os.listdir("train"):
    people.append(i)

# read images to validate
DIR_validate = "validate"
images = []
for img in os.listdir(DIR_validate):
    img_path = os.path.join(DIR_validate, img)
    img_read = cv.imread(img_path)
    im = [img_read, img]
    images.append(im)


# now running the model on every image 
c = 0
for [img, name] in images:

    na = ""
    for i in range(0, len(name)-1):
        na += name[i]

    c += 1
    img = resizeFrame(img, .4)
    grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    face_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=5)

    for (x,y,w,h) in face_rect:
        roi = grey[y:y+h, x:x+w]

        # now predict face label using face recognizer
        label, confidence = face_recognizer.predict(roi)

        # now printing label and confidence 
        print("original name is " + na + " predicted mane is :" + people[label] + " with a confidence of " + str(confidence))

        # now writing text on the image based on the prediction
        cv.putText(img, str(people[label]), (10,10), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.3, (0,0,255), thickness=2)

        # now drawing the rectangle around the face detected in the image
        cv.rectangle(img, (x,y), (x+w, y+h) , (255,255,255), thickness=2)

    # now display the image with predicted name
    cv.imshow(str(c), img)

cv.waitKey(0)