#import the required libraries 
import numpy as np 
import matplotlib.pyplot as plt 
import cv2 
%matplotlib inline 

# Read the image
image=cv2.imread("images/lenna.png")

# show Original image
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
print("         Original Color image")
plt.imshow(image)
plt.show()

#converting image to Gray scale 
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#plotting the grayscale image
plt.imshow(gray_image) 

#converting image to HSV format
hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

#plotting the HSV image
plt.imshow(hsv_image)