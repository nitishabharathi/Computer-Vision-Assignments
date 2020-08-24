import cv2
import numpy as np
import random

def convolve(img,mask):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m-1): 
        for j in range(1, n-1): 
            temp = img[i-1, j-1]*mask[0, 0]+img[i-1, j]*mask[0, 1]+img[i-1, j + 1]*mask[0, 2]+img[i, j-1]*mask[1, 0]+ img[i, j]*mask[1, 1]+img[i, j + 1]*mask[1, 2]+img[i + 1, j-1]*mask[2, 0]+img[i + 1, j]*mask[2, 1]+img[i + 1, j + 1]*mask[2, 2] 
            img_new[i, j]= temp 
    img_new = img_new.astype(np.uint8)
    return img_new


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

mask = np.ones((3, 3), dtype="float") * (1.0 / (3*3))
image = cv2.imread('pokemon.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("original", gray)
noiseimg = sp_noise(gray,0.05)
cv2.imshow("Noise Image", gray)
meanfilteroriginal = convolve(gray, mask)
cv2.imshow("Mean filter Original Image", meanfilteroriginal)
meanfilternoise = convolve(noiseimg, mask)
cv2.imshow("Mean filter Noise Image", meanfilternoise)
