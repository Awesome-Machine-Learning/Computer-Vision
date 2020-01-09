# 1.  Import required libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline

# 2. load the classifiers downloaded 
face_cascade1 = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
eye_cascade1 = cv2.CascadeClassifier('data/haarcascade_eye.xml')

# 3. read the image and convert to grayscale format
img1= cv2.imread('images/messi.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#plt.imshow(img1)

# 4. Calculate coordinates
faces1 = face_cascade1.detectMultiScale(gray1, 1.1, 4)
for (x,y,w,h) in faces1:
    cv2.rectangle(img1,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray1 = gray1[y:y+h, x:x+w]
    roi_color1 = img1[y:y+h, x:x+w]
    eyes1 = eye_cascade1.detectMultiScale(roi_gray1)
    
    #draw bounding boxes around detected features
    for (ex,ey,ew,eh) in eyes1:
        cv2.rectangle(roi_color1,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
# 5. plot the image
plt.imshow(img1)