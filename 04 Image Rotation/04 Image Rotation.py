#  Import the libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline

# read the image
image=cv2.imread("images/red.jpg")

# original color image
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

# plot original image
plt.imshow(image)

# image shape
print("image shape : ",image.shape)

# Select rows & columns for image
rows,cols=image.shape[:2]
print("Rows    :",rows)
print("Columns :",cols)

# (cols/2,rows/2) is the center of rotation for the image
# M is the cordinates of the center
# 180 degree rotation
M=cv2.getRotationMatrix2D((cols/2,rows/2),180,1) 

dst=cv2.warpAffine(image,M,(cols,rows))
plt.imshow(dst)