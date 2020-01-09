# 1. import the libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline

# 2. Read the image
image=cv2.imread("images/coin.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image)

# 3. converting RGB image to Binary
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray_image,127,255,0)

# 4. calculate the contours from binary image
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
with_contours=cv2.drawContours(image,contours,-1,(0,255,0),3)
plt.imshow(with_contours)