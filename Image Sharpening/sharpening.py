import cv2
import numpy as np
from matplotlib import pyplot as plt

img_act = cv2.imread('../data/baboon.png')
image_gray = cv2.cvtColor(img_act, cv2.COLOR_BGR2GRAY)
filtered_image = cv2.Canny(image_gray, threshold1=20, threshold2=200)

img = filtered_image + image_gray
stretch_img = ((img-img.min(axis=0))/(img.max(axis=0)-img.min(axis=0)))*255
plt.figure(figsize=(15,15))

plt.subplot(2,2,1),plt.imshow(image_gray,cmap = 'gray');
plt.title('Original')

plt.subplot(2,2,2),plt.imshow(filtered_image,cmap = 'gray');

plt.title('Canny Edge Detection')
plt.subplot(2,2,3),plt.imshow(img,cmap = 'gray');

plt.title('Added Image')
plt.subplot(2,2,4),plt.imshow(stretch_img,cmap = 'gray');
plt.title('Sharpened')
