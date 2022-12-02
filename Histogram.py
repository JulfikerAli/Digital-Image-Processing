import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path = 'animation.jpg'
    rgb = plt.imread(img_path)
    print(rgb.shape)
    
    red = rgb[:,:,0]
    green = rgb[:,:,1]
    blue = rgb[:,:,2]
    
    gray = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    
    th,bin = cv2.threshold(gray,120,255,cv2.THRESH_BINARY)
    print(th)
   
    img_set = [red, green, blue, gray, bin]
    title_set = ['RED', 'GREEN', 'BLUE', 'GRAY', 'BINARY']
    plt.figure(figsize=(20, 20))
    for i in range(len(img_set)):
        img = img_set[i]
        plt.subplot(2,3,i+1)
        plt.title(title_set[i])
        val = cv2.calcHist([img],[0],None,[256],[0,256])
        plt.plot(val)
        
    plt.savefig('Histogram.jpg')
    plt.show()
if __name__ == '__main__':
    main()