# 1. Import required libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline

# 2. Load the classifiers downloaded
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('data/haarcascade_eye.xml')

# 3. read the image and convert to grayscale format
img = cv2.imread('images/messi.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 4. Calculate coordinates
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)

    #draw bounding boxes around detected features
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

# 5. plot the image
plt.imshow(img)