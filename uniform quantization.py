import cv2

image = cv2.imread('pokemon.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(row,col) = gray.shape
print('Enter the number of gray levels in the output image')
level = int(input())
print('Press 1) Map to beginning 2)End')
mapp = int(input())
cv2.imshow("original",gray)
bins = int(256//level)
for i in range(row):
    for j in range(col):
        temp = int(gray[i][j]//bins)
        if mapp == 1:
            
            gray[i][j] = temp*bins
            
        elif mapp == 2:
            gray[i][j] = ((temp+1)*bins) - 1


cv2.imshow("",gray)
