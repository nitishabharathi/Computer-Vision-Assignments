import cv2
import numpy as np
from matplotlib import pyplot as plt

def histogram_stretch(img):
    stretch_img = ((img-img.min(axis=0))/(img.max(axis=0)-img.min(axis=0)))*255
    return stretch_img
    
img = cv2.imread('../data/lung.jpg',0)
stretch_img = histogram_stretch(img)
before_hist = np.ravel(img)
after_hist = np.ravel(stretch_img)

plt.figure(figsize=(15,10))
plt.subplot(2,2,1)
plt.title("Histogram of raw image")
plt.hist(before_hist,255)
plt.subplot(2,2,2)
plt.title("Actual image")
plt.imshow(img,cmap="gray")
plt.subplot(2,2,3)
plt.title("Histogram after stretching")
plt.hist(after_hist,255)
plt.subplot(2,2,4)
plt.title("Histogram stretched image")
plt.imshow(stretch_img,cmap="gray")
plt.show()
