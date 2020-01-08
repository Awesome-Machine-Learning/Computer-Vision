# 1. Import the libraries
import numpy as np 
import cv2 
import matplotlib.pyplot as plt 
%matplotlib inline

# 2. Read the images
image=cv2.imread("images/messi.jpg")
image1=cv2.imread("images/shoe2.jpg")
## original images
print(plt.imshow(image))
print(plt.imshow(image1))

# 3. calculate the edges using Canny edge algorithm
edges=cv2.Canny(image,100,200)
edges1=cv2.Canny(image1,100,200)
print(plt.imshow(edges))
print(plt.imshow(edges1))