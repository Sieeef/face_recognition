import os

import cv2

# import 'model'
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# specify which image has to be checked for faces
img = cv2.imread('images/7.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# check faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# create rectangle around faces and crop
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    faces = img[y:y + h, x:x + w]
    cv2.imshow("face", faces)
    cv2.imwrite('face.jpg', faces)

#display results
    cv2.imwrite('detcted.jpg', img)
    cv2.imshow('img', img)
    cv2.waitKey()

# safe faces in created folder
# cv2.imshow('img', img)
# cv2.waitKey()
