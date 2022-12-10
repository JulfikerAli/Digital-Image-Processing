import matplotlib.pyplot as plt
import numpy as np
import cv2

def main():
    img_path = 'animation.jpg'
    rgb = plt.imread(img_path)
    
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    print(grayscale.shape)
    
    def imageslice(img,bitPosition):
        row,col = img.shape
        slice = img.copy()
        for i in range(row):
            for j in range(col):
                slice[i,j]=img[i,j] & bitPosition
        return slice
    
    #plotting
    plt.figure(figsize=(30, 30))

    
    second_bit = imageslice(grayscale,128)
    plt.subplot(1,1,1)
    plt.title('Bit 8')
    plt.imshow(second_bit,cmap='gray')
    
    plt.savefig('Slice 8.jpg')
    plt.show()

if __name__ == '__main__':
    main()