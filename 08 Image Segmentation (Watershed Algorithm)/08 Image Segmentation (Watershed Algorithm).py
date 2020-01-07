# Import the libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline


# Read the image
image=cv2.imread("images/coin.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image)


# Convert image into Grayscale format n apply threshfold
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# plt.imshow(gray_image)
# Apply thresholding
ret,thresh=cv2.threshold(gray_image,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


# Get a kernel
kernel=np.ones((3,3),np.uint8)
# print(kernel)
opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)


# Extract the background from image
sure_bg=cv2.dilate(opening,kernel,iterations=3)
dist_transform=cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret,sure_fg=cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
sure_fg=np.uint8(sure_fg)
unknown=cv2.subtract(sure_bg,sure_bg)
ret,markers=cv2.connectedComponents(sure_fg)
markers=markers+1
markers[unknown==255]=0
markers=cv2.watershed(image,markers)
image[markers==1]=[255,0,0]

plt.imshow(sure_bg)
plt.imshow(sure_fg)