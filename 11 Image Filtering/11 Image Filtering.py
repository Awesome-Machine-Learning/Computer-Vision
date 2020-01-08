# 1. Import the libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline

# 2. Read the image
image=cv2.imread("images/Lenna.png")
## original image
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image)

# 3. using the averaging kernel for image smoothening
M = np.float32([[1,0,-100],[0,1,-100]]) 
rows,cols = image.shape[:2] 
kernel = np.ones((3,3),np.uint8)
dst = cv2.warpAffine(image,M,(cols,rows)) 
averaging_kernel=np.ones((3,3),np.float32)/9
filtered_image=cv2.filter2D(image,-1,kernel)

gaussian_kernel_x = cv2.getGaussianKernel(5,1) 
gaussian_kernel_y = cv2.getGaussianKernel(5,1) 

##converting to two dimensional kernel using matrix multiplication 
gaussian_kernel = gaussian_kernel_x * gaussian_kernel_y.T 

##you can also use cv2.GaussianBLurring(image,(shape of kernel),standard deviation) instead of cv2.filter2D 
filtered_image = cv2.filter2D(image,-1,gaussian_kernel) 
plt.imshow(filtered_image)