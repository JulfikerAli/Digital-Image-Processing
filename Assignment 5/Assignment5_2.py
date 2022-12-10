import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path = 'animation.jpg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    print(gray.shape)

    def imageslice(image,pos):
        row = image.shape[0]
        col = image.shape[1]
        slice = image.copy()
        for i in range(row):
            for j in range(col):
                slice[i][j] = image[i][j] & pos
        return slice
    
    title_set = ['Bit 1','Bit 2','Bit 3','Bit 4','Bit 5','Bit 6','Bit 7','Bit 8']
    p = 1
    for i in range(len(title_set)):
        plt.subplot(1,1,1)
        plt.title(title_set[3])
        if(i == 0):
            p = 1
        else:
            p = p * 2 
        val = imageslice(gray,p)
        plt.imshow(val,cmap='gray')
        plt.savefig('Bit 3.jpg')
    
    plt.show()
    
if __name__ == '__main__':
    main()