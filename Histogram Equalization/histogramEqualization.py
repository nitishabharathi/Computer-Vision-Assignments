import numpy as np
from matplotlib import pyplot as plt
import cv2

def get_histogram(image, bins):
    histogram = np.zeros(bins)
    for pixel in image:
        histogram[pixel] += 1
    return histogram

def cumsum(a):
    a = iter(a)
    b = [next(a)]
    for i in a:
        b.append(b[-1] + i)
    return np.array(b)

def HistogramEqualization(img):
    img = np.asarray(img);
    flat = img.flatten();
    hist = get_histogram(flat, 256)
    cs = cumsum(hist)
    nj = (cs - cs.min()) * 255
    N = cs.max() - cs.min()
    cs = nj / N
    cs = cs.astype('uint8')
    img_new = cs[flat]
    img_new = np.reshape(img_new, img.shape)
    img_hist = np.ravel(img)
    img_new_hist = np.ravel(img_new)
    return img_new,img_hist,img_new_hist
    
img = cv2.imread('../data/lung.jpg')
img_new,img_hist,img_new_hist = HistogramEqualization(img)

plt.figure(figsize=(15,10))
plt.subplot(2,2,1)
plt.title("Histogram of raw image")
plt.hist(img_hist,255)
plt.subplot(2,2,2)
plt.title("Actual image")
plt.imshow(img,cmap="gray")
plt.subplot(2,2,3)
plt.title("Histogram after Equalization")
plt.hist(img_new_hist,255)
plt.subplot(2,2,4)
plt.title("Histogram Equalized image")
plt.imshow(img_new,cmap="gray")
plt.show()
plt.savefig('histogramEqualization.jpeg')
