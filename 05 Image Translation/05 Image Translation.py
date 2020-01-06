#  Import the libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline

# Read the image
image=cv2.imread("images/messi.jpg")

# show original image
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.show()

# shifting the image 100 pixels in both dimensions
image.shape

# select rows n cols for transformation
rows,cols=image.shape[:2]

# select cordinate for transformation
M=np.float32([[1,0,-100],[0,1,-100]])
M

# transformation
dst=cv2.warpAffine(image,M,(cols,rows))
plt.imshow(dst)

