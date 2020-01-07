# Import the libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline


# Read the image
image=cv2.imread("images/messi.jpg",0)
# show the image
plt.imshow(image)
plt.show()


# make diffrent styles
# Binary style
ret,thresh_binary=cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)
# Binary Inv
ret, thresh_binary_inv=cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY_INV)
# Trunc
ret,thresh_trunc=cv2.threshold(gray_image,127,255,cv2.THRESH_TRUNC)
# Tozero
ret,thresh_tozero=cv2.threshold(gray_image,127,255,cv2.THRESH_TOZERO)
# Tozero_inv
ret,thresh_tozero_inv=cv2.threshold(gray_image,127,255,cv2.THRESH_TOZERO_INV)


# Diaplaying the diffrent Thresholding Styles
names = ['Oiriginal Image','BINARY','THRESH_BINARY_INV','THRESH_TRUNC','THRESH_TOZERO','THRESH_TOZERO_INV']
images=gray_image,thresh_binary,thresh_binary_inv,thresh_trunc,thresh_tozero,thresh_tozero_inv
# plot all the style images
plt.figure(figsize=(16,9))
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(names[i])
    plt.xticks([])
    plt.yticks([])
plt.show()