import cv2
import numpy as np


def convolve(img,mask):
    m, n = img.shape
    img_new = np.zeros([m, n])
    for i in range(1, m-1): 
        for j in range(1, n-1): 
            temp = img[i-1, j-1]*mask[0, 0]+img[i-1, j]*mask[0, 1]+img[i-1, j + 1]*mask[0, 2]+img[i, j-1]*mask[1, 0]+ img[i, j]*mask[1, 1]+img[i, j + 1]*mask[1, 2]+img[i + 1, j-1]*mask[2, 0]+img[i + 1, j]*mask[2, 1]+img[i + 1, j + 1]*mask[2, 2] 
            img_new[i, j]= temp 
    img_new = img_new.astype(np.uint8)
    return img_new

mean1 = np.ones((3, 3), dtype="float") * (1.0 / (3*3))
mean2 = np.array(([1,1,1],[1, 2, 1],[1, 1, 1]), dtype="float")
mean2 = mean2 * (1.0/np.sum(mean2))
mean3 = np.array(([1,2,1],[2, 4, 2],[1, 2, 1]), dtype="float")
mean3 = mean3 * (1.0/np.sum(mean3))

enhance1 = np.array(([-1,-1,-1],[-1, 9, -1],[-1, -1, -1]), dtype="int")
enhance2 = np.array(([1,-1,1],[-2, 5, -2],[1, -2, 1]), dtype="int")
enhance3 = np.array(([0,-2,0],[-1, 5, -1],[0, -1, 0]), dtype="int")


kernelBank = (        	
        ("mean filter 1",mean1),
        ("mean filter 2",mean2),
        ("mean filter 3",mean3),
        ("enchancement filter 1",enhance1),
        ("enchancement filter 2",enhance2),
        ("enchancement filter 3",enhance3),
)
image = cv2.imread('pokemon.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


for (kernelName, kernel) in kernelBank:
    print("[INFO] applying {} kernel".format(kernelName))
    cv2.imshow("original", gray)
    convoleOutput = convolve(gray, kernel)    
    cv2.imshow("{} - convole".format(kernelName), convoleOutput)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
