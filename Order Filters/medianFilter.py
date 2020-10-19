import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

def convolve_median(img):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m-1): 
        for j in range(1, n-1): 
            temp = [img[i-1, j-1], 
                   img[i-1, j], 
                   img[i-1, j + 1], 
                   img[i, j-1], 
                   img[i, j], 
                   img[i, j + 1], 
                   img[i + 1, j-1], 
                   img[i + 1, j], 
                   img[i + 1, j + 1]] 
          
            temp = sorted(temp) 
            img_new[i, j]= temp[4] 
    img_new = img_new.astype(np.uint8)
    return img_new

img = cv2.imread('../data/pokemon.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
noise_img = sp_noise(img,0.05)
convoleMedianOutput = convolve_median(noise_img)

plt.figure(figsize=(20,15))
plt.subplot(1,2,1),plt.imshow(noise_img,cmap = 'gray');
plt.title('Noise')
plt.subplot(1,2,2),plt.imshow(convoleMedianOutput,cmap = 'gray');
plt.title('Median Filter')
