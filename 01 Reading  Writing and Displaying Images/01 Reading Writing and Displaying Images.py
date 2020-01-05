#import the libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2
%matplotlib inline

image=cv2.imread("images/rw3.png")

# original color of image
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

# plotting the image
plt.imshow(image)

# save into test_images folder
cv2.imwrite("images/test_images/test_cat.jpg",image)