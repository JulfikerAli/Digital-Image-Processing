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
    mask[250:450,620:850] = 255
    
    sliced_bit = cv2.bitwise_and(grayscale,mask)
    

   
    plt.subplot(1,1,1)
    plt.title('Binary Masked Image')
    plt.imshow(sliced_bit,cmap='gray')
    plt.savefig('Binary Masked Image.jpg')
    plt.show()
    
if __name__ == '__main__':
    main()