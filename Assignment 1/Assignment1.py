import matplotlib.pyplot as plt
import numpy as np
import cv2


img_path = 'animation.jpg'
image = plt.imread(img_path)
r,g,b = image[:,:,0],image[:,:,1],image[:,:,2]

grayscale = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

row,col = grayscale.shape
binary = np.zeros((row,col),dtype=np.uint8)

threshold = 127
for i in range (row):
    for j in range (col):
        if grayscale[i][j]>=threshold:
            binary[i][j]=grayscale[i][j]


img_set = [image,grayscale,r,g,b,binary]
title_set = ['RGB','Grayscale','Red','Green','Blue','Binary']
cmap_set = ['','gray','Reds','Greens','Blues','binary']

n = len(img_set)
plt.figure(figsize=(15,15))

for i in range (1):
    img = img_set[4]
    plt.subplot(1,1,1)
    plt.title(title_set[4])
    ch = len(img_set[4].shape)
    if ch == 3:
        plt.imshow(img_set[4])
    else:
        plt.imshow(img_set[4],cmap=cmap_set[4])

    plt.savefig('image_Blue.jpg')
plt.show()
