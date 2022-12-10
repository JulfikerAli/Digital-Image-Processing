import matplotlib.pyplot as plt
import numpy as np
import cv2

def conv(matrix,kernel):
    row = matrix.shape[0]
    col = matrix.shape[1]
    
    r = 2
    c = 2
    new_img = np.zeros((row - r,col - c),dtype=np.uint8)
    for i in range(row - r):
        for j in range(col - c):
            temp = np.sum(np.multiply(matrix[i:3+i,j:3+j],kernel))
            if temp > 255:
                new_img[i][j] = 255
            elif temp < 0:
                new_img[i][j] = 0
            else:
                new_img[i][j] = temp
    return new_img
    
def main():
    img_path = 'animation.jpg'
    rgb = plt.imread(img_path)
    
    grayscale = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    kernel = np.array([
        [-1,-1,-1],
        [-1,8,-1],
        [-1,-1,-1]
    ])
    val1 = conv(grayscale,kernel)
    val2 = cv2.filter2D(grayscale,-1,kernel)
    
   
    plt.subplot(1,1,1)
    plt.title('Built In Function')
    plt.imshow(val1,cmap='gray')
    
    
    plt.savefig('Built In Neighbourhood.jpg')
    plt.show()
    
if __name__ == '__main__':
    main()