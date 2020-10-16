import cv2
import numpy as np
from matplotlib import pyplot as plt

def histogram_sliding(image,offset):
    return image + offset 
    
img = cv2.imread('../data/lung.jpg',0)
slide_img = histogram_sliding(img,30)

before_hist = np.ravel(img)
after_hist = np.ravel(slide_img)

plt.figure(figsize=(15,10))
plt.subplot(2,2,1)
plt.title("Histogram of raw image")
plt.hist(before_hist,255)
plt.subplot(2,2,2)
plt.title("Actual image")
plt.imshow(img,cmap="gray")
plt.subplot(2,2,3)
plt.title("Histogram after Sliding")
plt.hist(after_hist,255)
plt.subplot(2,2,4)
plt.title("Histogram Slided Image")
plt.imshow(slide_img,cmap="gray")
plt.show()
