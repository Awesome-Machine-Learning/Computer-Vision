# import the libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline

# Read the image in gray Scale
gray_image=cv2.imread("images/balls1.jpg",0)


# make diffrent styles
# Global threshholding
ret,thresh_global=cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY
# thresh_mean
#here 11 is the pixel neighbourhood that is used to calculate the threshold value
thresh_mean=cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
# Gaussian thresh
thresh_gaussian=cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

                              
# plot all the style images                                
names=['Original Image','Global Thresholding','Adaptive Mean Threshold','Adaptive Gaussian Thresholding']
images=[gray_image,thresh_global,thresh_mean,thresh_gaussian]

plt.figure(figsize=(16,9))
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(names[i],fontsize=20)
    plt.xticks([])
    plt.yticks([])
    
plt.show()                               
                                
                                
                                