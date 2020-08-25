import cv2
import random
import numpy as np

image = cv2.imread('pokemon.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_copy = gray
height,width = gray.shape


print('original shape',width,height)
w = int(input('Enter the width of the output image'))
h = int(input('Enter the height of the output image'))

col_del = width - w
row_del = height - h


for i in range(row_del):
    k = random.randint(0,height-1)
    gray_copy = np.delete(gray_copy,k,0)
    height = height - 1

for i in range(col_del):
    k = random.randint(0,width-1)
    gray_copy = np.delete(gray_copy,k,1)
    width = width - 1
w_new,h_new = gray_copy.shape

print('decimation shape',w_new,h_new)   

cv2.imshow("original", gray)
cv2.imshow("Decimation", gray_copy)
