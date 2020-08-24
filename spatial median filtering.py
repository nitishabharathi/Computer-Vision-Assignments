import cv2
import numpy as np


def convolve_mean(img,mask):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m-1): 
        for j in range(1, n-1): 
            temp = img[i-1, j-1]*mask[0, 0]+img[i-1, j]*mask[0, 1]+img[i-1, j + 1]*mask[0, 2]+img[i, j-1]*mask[1, 0]+ img[i, j]*mask[1, 1]+img[i, j + 1]*mask[1, 2]+img[i + 1, j-1]*mask[2, 0]+img[i + 1, j]*mask[2, 1]+img[i + 1, j + 1]*mask[2, 2] 
            img_new[i, j]= temp 
    img_new = img_new.astype(np.uint8)
    return img_new
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


mask = np.ones((3, 3), dtype="float") * (1.0 / (3*3))
image = cv2.imread('pokemon.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("original", gray)
convoleMeanOutput = convolve_mean(gray,mask) 
cv2.imshow("Mean Filter Image", convoleMeanOutput)
convoleMedianOutput = convolve_median(gray) 
cv2.imshow("Median Filter Image", convoleMedianOutput)

