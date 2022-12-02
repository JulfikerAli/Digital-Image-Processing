import matplotlib.pyplot as plt
import cv2
import numpy as np
import random


def main():
    img_path = 'animation.jpg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    print(gray.shape)
    
    row = gray.shape[0]
    col = gray.shape[1]
    
    left = gray.copy()
    right = gray.copy()
    band = gray.copy()
    
    left = left - 69
    right = right + 20
    
    for i in range(row):
        for j in range(col):
            if(band[i][j] <= 100):
                band[i][i] = 100
            elif(band[i][j] >= 175):
                band[i][j] = 175
                
    grayhist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    lefthist = cv2.calcHist([left], [0], None, [256], [0, 256])
    righthist = cv2.calcHist([right], [0], None, [256], [0, 256])
    bandhist = cv2.calcHist([band], [0], None, [256], [0, 256])
    
    plt.figure(figsize=(15, 15))
    plt.subplot(2, 4, 1)
    plt.title('Original')
    plt.imshow(gray, cmap='gray')
    plt.subplot(2, 4, 2)
    plt.title('Original')
    plt.plot(grayhist)
    plt.subplot(2, 4, 3)
    plt.title('Moved Right')
    plt.imshow(right, cmap='gray')
    plt.subplot(2, 4, 4)
    plt.title('Moved Right')
    plt.plot(righthist)
    plt.subplot(2, 4, 5)
    plt.title('Moved Left')
    plt.imshow(left, cmap='gray')
    plt.subplot(2, 4, 6)
    plt.title('Moved Left')
    plt.plot(lefthist)
    plt.subplot(2, 4, 7)
    plt.title('Narrow band')
    plt.imshow(band, cmap='gray')
    plt.subplot(2, 4, 8)
    plt.title('NarrowBand hist')
    plt.plot(bandhist)
    
    plt.savefig('Histogram_Shifting.jpg')
    
    plt.show()
    
    
    
    
if __name__ == '__main__':
    main()