import cv2

image = cv2.imread('pokemon.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(row,col) = gray.shape
low1 = int(input('Enter lower end of range1'))
high1 = int(input('Enter higher end of range1'))
map1 = int(input('Enter map value range1'))

low2 = int(input('Enter lower end of range2'))
high2 = int(input('Enter higher end of range2'))
map2 = int(input('Enter map value range2'))

low3 = int(input('Enter lower end of range3'))
high3 = int(input('Enter higher end of range3'))
map3 = int(input('Enter map value range3'))


low4 = int(input('Enter lower end of range4'))
high4 = int(input('Enter higher end of range4'))
map4 = int(input('Enter map value range4'))

cv2.imshow("original",gray)

for i in range(row):
    for j in range(col):
        if gray[i][j]>=low1 and gray[i][j]<=high1:
            gray[i][j] = map1
        elif gray[i][j]>=low2 and gray[i][j]<=high2:
            gray[i][j] = map2
        elif gray[i][j]>=low3 and gray[i][j]<=high3:
            gray[i][j] = map3
        elif gray[i][j]>=low4 and gray[i][j]<=high4:
            gray[i][j] = map4


cv2.imshow("",gray)

