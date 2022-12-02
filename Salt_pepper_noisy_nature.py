from random import random
import matplotlib.pyplot as plt
import numpy as np
import cv2
import random

def main():
    img_path = 'animation.jpg'
    rgb = plt.imread(img_path)
    
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    print(grayscale.shape)
    
    row = grayscale.shape[0]
    col = grayscale.shape[1]  
    img = grayscale.copy()
    
    number_of_pixels = random.randint(100,row*100+col*10)
    for i in range(number_of_pixels):
        y = random.randint(0,row - 1)
        x = random.randint(0,col - 1)
        img[y][x] = 255
    
    for i in range(number_of_pixels):
        y = random.randint(0,row - 1)
        x = random.randint(0,col - 1)
        img[y][x] = 0
    
    
    processed_img1 = cv2.blur(grayscale, (5, 5))
    processed_img2 = cv2.blur(img, (5, 5))
    processed_img3 = cv2.GaussianBlur(img, (5, 5), 0)
    processed_img4 = cv2.medianBlur(img, 3) 
        

    plt.figure(figsize=(30,30))
    plt.subplot(2,3,1)
    plt.title('Grayscale')
    plt.imshow(grayscale,cmap='gray')
    
    plt.subplot(2, 3, 2)
    plt.title('Filtered Image(Averaging)')
    plt.imshow(processed_img1, cmap='gray')
    
    plt.subplot(2, 3, 3)
    plt.title('Noisy Image(Salt & pepper noise)')
    plt.imshow(img, cmap='gray')
    
    plt.subplot(2, 3, 4)
    plt.title('Filtered Noisy Image(Averaging)')
    plt.imshow(processed_img2, cmap='gray')
    
    plt.subplot(2, 3, 5)
    plt.title('Filtered Noisy Image(Gaussian Kernel)')
    plt.imshow(processed_img3, cmap='gray')
    
    plt.subplot(2, 3, 6)
    plt.title('Filtered Noisy Image(Median Filter)')
    plt.imshow(processed_img4, cmap='gray')
    plt.savefig('Salt_pepper_noisy_nature.jpg')
    plt.show()
    
if __name__ == '__main__':
    main()