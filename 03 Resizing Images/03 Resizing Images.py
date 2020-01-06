#import the required libraries 
import numpy as np 
import matplotlib.pyplot as plt 
import cv2 
%matplotlib inline 

# read the image
image=cv2.imread("images/messi.jpg")

# original color image
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

#converting image to size (100,100,3) 
smaller_image = cv2.resize(image,(100,100),inerpolation='linear') 

#plot the resized image
plt.imshow(smaller_image)