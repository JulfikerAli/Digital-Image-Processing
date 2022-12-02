import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path = 'animation.jpg'
    image = plt.imread(img_path)
    grayscale = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    print(grayscale.shape)
    row = grayscale.shape[0]
    col = grayscale.shape[1]
    
    mask = np.zeros((row,col),dtype=np.uint8)
    mask[100:200,200:300] = 255
    
    sliced_bit = cv2.bitwise_and(grayscale,mask)
    

    plt.subplot(2,1,1)
    plt.title('Gray')
    plt.imshow(grayscale,cmap='gray')
    plt.subplot(2,1,2)
    plt.title('Binary Mask')
    plt.imshow(sliced_bit,cmap='gray')
    plt.savefig('Binary_Mask.jpg')
    plt.show()
    
if __name__ == '__main__':
    main()