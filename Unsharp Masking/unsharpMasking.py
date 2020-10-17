import cv2
import numpy as np
from matplotlib import pyplot as plt

def unsharp_mask(img,shrink_min,shrink_max):
    m, n = img.shape 
    mask = np.ones([3, 3], dtype = int) 
    mask = mask / 9
    
    img_new = np.zeros([m, n]) 

    for i in range(1, m-1): 
        for j in range(1, n-1): 
            temp = img[i-1, j-1]*mask[0, 0]+img[i-1, j]*mask[0, 1]+img[i-1, j + 1]*mask[0, 2]+img[i, j-1]*mask[1, 0]+ img[i, j]*mask[1, 1]+img[i, j + 1]*mask[1, 2]+img[i + 1, j-1]*mask[2, 0]+img[i + 1, j]*mask[2, 1]+img[i + 1, j + 1]*mask[2, 2] 
            img_new[i, j]= temp 
    
    img_new = img_new.astype(np.uint8) 
    shrink_img = (((shrink_max-shrink_min)/(img_new.max(axis=0)-img_new.min(axis=0)))*(img_new-img_new.min(axis=0)))+shrink_min
    img = img-shrink_img
    stretch_img = ((img-img.min(axis=0))/(img.max(axis=0)-img.min(axis=0)))*255
    return stretch_img
    
img = cv2.imread('../data/baboon.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
unsharp_img = unsharp_mask(img,0,100)

plt.figure(figsize=(20,20))
plt.subplot(1,2,1)
plt.title("Original image")
plt.imshow(img,cmap="gray")
plt.subplot(1,2,2)
plt.title("Unsharp Mask")
plt.imshow(unsharp_img,cmap="gray")   
