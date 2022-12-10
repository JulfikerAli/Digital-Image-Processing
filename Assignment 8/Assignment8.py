import matplotlib.pyplot as plt
import numpy as np
import cv2
import random

def main():
    img_path = 'animation.jpg'
    rgb = plt.imread(img_path)
    grayscale = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    th,binary1 = cv2.threshold(grayscale,125,255,cv2.THRESH_BINARY)
    binary2 = np.array([
        [1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 0, 0]
    ],dtype=np.uint8)
    kernel = np.array([
        [0,1,0],
        [1,1,1],
        [0,1,0]
    ],dtype=np.uint8)
    
    erosion1 = cv2.erode(binary1,kernel,iterations=1)
    dilation1 = cv2.dilate(binary1,kernel,iterations=1)
    opening1 = cv2.morphologyEx(binary1,cv2.MORPH_OPEN,kernel)
    closing1 = cv2.morphologyEx(binary1,cv2.MORPH_CLOSE,kernel)
    
    erosion2 = cv2.erode(binary2,kernel,iterations=1)
    dilation2 = cv2.dilate(binary2,kernel,iterations=1)
    opening2 = cv2.morphologyEx(binary2,cv2.MORPH_OPEN,kernel)
    closing2 = cv2.morphologyEx(binary2,cv2.MORPH_CLOSE,kernel)    
    
    plt.subplot(1, 1, 1)
    plt.title('Dilation')
    plt.imshow(dilation1,cmap='gray')
    
    plt.savefig('morph_dialation')
    
    plt.show()
if __name__ == '__main__':
    main()