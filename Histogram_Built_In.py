from typing import Counter
import matplotlib.pyplot as plt 
import numpy as np
import cv2

img_path = 'animation.jpg'
image = plt.imread(img_path)
grayscale = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

hist_b, bins = np.histogram(image, 256)

hist_u = []
for i in range(256):
    hist_u += [np.count_nonzero(image == i)]

img_set = [image,grayscale,hist_b,hist_u]
title_set = ['RGB','Grayscale','Built_in','Custom']
cmap_set = ['','gray','gray','gray']

n = len(img_set)
plt.figure(figsize=(15,15))

for i in range (n):
    img = img_set[i]
    plt.subplot(2,3,i+1)
    plt.title(title_set[i])
    ch = len(img_set[i].shape)
    if ch == 3:
        plt.imshow(img_set[i])
    else:
        plt.imshow(img_set[i],cmap=cmap_set[i])

    plt.savefig('Histogram_Comparision.jpg')
plt.show()
