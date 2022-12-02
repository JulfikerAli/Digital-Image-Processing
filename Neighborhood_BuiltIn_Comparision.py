import numpy as np
import matplotlib.pyplot as plt 
import cv2

image = plt.imread('animation.jpg')
grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) 

g_width = grayscale.shape[0]
g_height = grayscale.shape[1]

kernel1 = np.array([[-1, -1, -1],[-1, 8, -1],[-1, -1, -1]])

pad_quantity = int((len(kernel1) - 1) / 2)

padded_g = pad_arr = np.pad(grayscale, pad_quantity)

processed_img1 = cv2.filter2D(padded_g, -1, kernel1, cv2.BORDER_CONSTANT)
processed_img1 = processed_img1[pad_quantity:g_width+pad_quantity, pad_quantity:g_height+pad_quantity]

print(padded_g[0:5,padded_g.shape[1]-5:])
print(processed_img1)

m, n = kernel1.shape

y, x = padded_g.shape

processed_img2 = np.zeros((g_width, g_height))

for i in range(g_width):
    for j in range(g_height):
        processed_img2[i][j] = int(np.sum(padded_g[i:i+m, j:j+n]*kernel1))

        if(processed_img2[i][j] > 255):
            processed_img2[i][j] = 255
        if(processed_img2[i][j] < 0):
            processed_img2[i][j] = 0

img_set = [image,grayscale,processed_img1, processed_img2]
title_set = ['RGB','Grayscale','Neighborhood', 'BuiltIn']
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

    plt.savefig('Neighborhood_BuiltIn_Comparision.jpg')
plt.show()
