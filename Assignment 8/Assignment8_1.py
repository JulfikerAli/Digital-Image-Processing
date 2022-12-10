import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path='animation.jpg'
    img=plt.imread(img_path)
    grayscale=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    _,binary=cv2.threshold(grayscale,50,255,cv2.THRESH_BINARY)

    kernel = np.ones((5, 5), np.uint8)
    img_erosion = cv2.erode(binary, kernel, iterations=1)
    img_dilation = cv2.dilate(binary, kernel, iterations=1)
    opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)


    img_set=[img,binary,img_erosion,img_dilation,opening,closing]
    title_set=['original','binary','img_erosion','img_dilation','opening','closing']
    cmap_set = ['','gray','gray','gray','gray','gray']
    
    n = len(img_set)
    plt.figure(figsize=(20,20))

    for i in range(1):
        plt.subplot(1,1,1)
        plt.title(title_set[5])
        ch=len(img_set[5].shape)
    if (ch==3):
        plt.imshow(img_set[5])
    else:
        plt.imshow(img_set[5],cmap=cmap_set[5])
        plt.subplots_adjust(wspace=1,hspace=1)
    plt.savefig('Closing.jpg')
    plt.show()
if __name__=='__main__':
    main()
