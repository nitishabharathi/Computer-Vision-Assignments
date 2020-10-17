import cv2
import numpy as np
import matplotlib.pyplot as plt

def find_nearest_above(my_array, target):
    diff = my_array - target
    mask = np.ma.less_equal(diff, -1)
    if np.all(mask):
        c = np.abs(diff).argmin()
        return c 
    masked_diff = np.ma.masked_array(diff, mask)
    return masked_diff.argmin()

def hist_match(original, specified):
    oldshape = original.shape
    original = original.ravel()
    specified = specified.ravel()
    s_values, bin_idx, s_counts = np.unique(original, return_inverse=True,return_counts=True)
    t_values, t_counts = np.unique(specified, return_counts=True)
    s_quantiles = np.cumsum(s_counts).astype(np.float64)
    s_quantiles /= s_quantiles[-1]
    t_quantiles = np.cumsum(t_counts).astype(np.float64)
    t_quantiles /= t_quantiles[-1]
    sour = np.around(s_quantiles*255)
    temp = np.around(t_quantiles*255)
    
    b=[]
    for data in sour[:]:
        b.append(find_nearest_above(temp,data))
    b= np.array(b,dtype='uint8')
    return b[bin_idx].reshape(oldshape)
    
    
specified = cv2.imread('../data/albert.jpg',0)
original = cv2.imread('../data/lung.jpg',0)
a = hist_match(original, specified)
hist_original = np.ravel(original)
hist_specified = np.ravel(specified)
hist_output = np.ravel(a)

plt.figure(figsize=(15,10))
plt.subplot(3,2,1)
plt.title("Histogram of Original image")
plt.hist(hist_original,255)
plt.subplot(3,2,2)
plt.title("Original image")
plt.imshow(original,cmap="gray")
plt.subplot(3,2,3)
plt.title("Histogram of Specified Image")
plt.hist(hist_specified,255)
plt.subplot(3,2,4)
plt.title("Specified Image")
plt.imshow(specified,cmap="gray")
plt.subplot(3,2,5)
plt.title("Output Histogram")
plt.hist(hist_output,255)
plt.subplot(3,2,6)
plt.title("Output Image")
plt.imshow(np.array(a,dtype='uint8'),cmap ='gray')
plt.show()
