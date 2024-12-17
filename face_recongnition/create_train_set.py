import cv2 as cv
import numpy as np
import os

# list of people

people = []
for i in os.listdir("train"):
    people.append(i)

# testing

# dire = "train"
# path = os.path.join(dire, people[0])
# im_path = os.path.join(path, os.listdir(path)[0])
# ima = cv.imread(im_path)
# ima = resizeFrame(ima, .4)
# cv.imshow("first image ", ima)


# print(people)

DIR = "train"

features = []
labels = []

# getting the haar_cascade file in na variable
haar_cascade = cv.CascadeClassifier("../models/harr_face.xml")

# training over data set
def create_training():

    # looping over each person directory
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        # c = 0
        # looping over each image in the directory
        for img in os.listdir(path):
            # c = c + 1
            # if (c > 2):
            #     break
            img_path = os.path.join(path, img)

            print(img_path)
            # now reading the image
            image = cv.imread(img_path)
            # cv.imshow(img_path ,image)
            # image = resizeFrame(image, .4)

            # convert to grey scale
            grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

            # now providing image to the model and getting the rectangle' dimention
            face_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=3)

            # now looping over the face_rect list to get the touple (x,y,w,h) for the face
            for (x,y,w,h) in face_rect:
                roi = grey[y:y+h, x:x+w]
                features.append(roi)
                labels.append(label)


create_training()

print("training done----------------------------------------")

# print("features : " + str(len(features)))
# print("labels : " + str(len(labels)))

# cv.waitKey(0)


# instace of face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# converting features and labels to numpy arrays
features = np.array(features, dtype="object")
labels = np.array(labels)

# train the recognizer of features and lables list
face_recognizer.train(features,labels)

# now saving the features and labels list in seperate files
np.save("features.npy", features)
np.save("labels,npy", labels)

# saving the trainde model in a yml file 
face_recognizer.save("face_trained.yml")


