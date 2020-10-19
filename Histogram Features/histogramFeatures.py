import numpy as np
from matplotlib import pyplot as plt
import cv2
import math
import pandas as pd

def histogram_features(img_hist):
    gray_level = [0] * 256

    for i in img_hist:
        gray_level[i] += 1   
    Pg = [x / len(img_hist) for x in gray_level]
    mean = sum(img_hist)/len(img_hist)
    
    var = 0
    for i in range(len(gray_level)):
        var += ((gray_level[i] - mean)**2)*Pg[i]
    std = math.sqrt(var)

    skew = 0
    for i in range(len(gray_level)):
        skew += ((gray_level[i] - mean)**3)*Pg[i]
    skew = skew/(std**3)
    
    energy = 0
    for i in Pg:
        energy += i**2
   
    entropy = 0

    for i in Pg:
        try:
            entropy += i * math.log(i,2)
        except:
            continue
    entropy = entropy * -1
    return mean,std,skew,energy,entropy
    
    
img2 = cv2.imread("../input/cv-image/image.png")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img_hist2 = np.ravel(img2)
img3 = cv2.imread('../input/cv-image/image (1).png')
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
img_hist3 = np.ravel(img3)


plt.figure(figsize=(20,15))
plt.subplot(2,2,1),plt.imshow(img2,cmap = 'gray');
plt.title('High Contrast')
plt.subplot(2,2,2),plt.imshow(img3,cmap = 'gray');
plt.title('Low Contrast')
plt.subplot(2,2,3),plt.hist(img_hist2,255);
plt.subplot(2,2,4),plt.hist(img_hist3,255);

mean1, std1, skew1,energy1,ent1 = histogram_features(img_hist2)
mean2, std2, skew2,energy2,ent2 = histogram_features(img_hist3)

mean = [mean1,mean2]
std = [std1,std2]
skew = [skew1,skew2]
energy = [energy1,energy2]
entropy = [ent1,ent2]
img_names = ['Baboon High Contrast','Baboon Low Contrast']
df = pd.DataFrame(list(zip(img_names, mean,std,skew,energy,entropy)), columns =['Img Name', 'Mean','Std','Skew','Energy','Entropy']) 
print(df)
