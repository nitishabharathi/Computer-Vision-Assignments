import numpy as np
from matplotlib import pyplot as plt
import cv2

def robertsEdgeDetector(img):
    m,n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1,m-1):
        for j in range(1,n-1):
            img_new[i][j] = abs(img[i][j] - img[i-1][j-1]) + abs(img[i][j-1] - img[i-1][j])
    return img_new
    
def hist_equalization(img):
    flat = img.flatten();
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
    hist = get_histogram(flat, 256)
    cs = cumsum(hist)
    nj = (cs - cs.min()) * 255
    N = cs.max() - cs.min()
    cs = nj / N
    cs = cs.astype('uint8')
    img_new = cs[flat]


    img_new = np.reshape(img_new, img.shape)
    return img_new
    
def edgeSharpeningAlgorithm1(img,shrink_min,shrink_max):
    shrink_img = hist_shrink(img,shrink_min,shrink_max)
    img_new = robertsEdgeDetector(shrink_img)
    img_added = img_new + img
    img = img_added.astype('int8')
    img = hist_equalization(img)
    return img_new,img_added,img
    
img_act = cv2.imread('../data/baboon.png')
image_gray = cv2.cvtColor(img_act, cv2.COLOR_BGR2GRAY)
robert,added, final = edgeSharpeningAlgorithm1(image_gray,10,100)

plt.figure(figsize=(10,10))
plt.subplot(2,2,1),plt.imshow(image_gray,cmap = 'gray');
plt.title('Original')
plt.subplot(2,2,2),plt.imshow(robert,cmap = 'gray');
plt.title('Roberts Edge Detection')
plt.subplot(2,2,3),plt.imshow(added,cmap = 'gray');
plt.title('Added Image')
plt.subplot(2,2,4),plt.imshow(final,cmap = 'gray');
plt.title('Sharpened')
