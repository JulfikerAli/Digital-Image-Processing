import matplotlib.pyplot as plt
import cv2
import numpy as np
import math


def main():
    img_path = 'animation.jpg'
    image = plt.imread(img_path)
    
    c = 5
    p = 1
    epsilon = 0.0000001
    T1 = 50
    T2 = 100

    grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    row, col = grayscale.shape

    processed_img1 = np.zeros((row, col), dtype=np.uint8)
    processed_img2 = np.zeros((row, col), dtype=np.uint8)
    processed_img3 = np.zeros((row, col), dtype=np.uint8)
    processed_img4 = np.zeros((row, col), dtype=np.uint8)

    for x in range(row):
        for y in range(col):
            r = grayscale[x, y]
            if r >= T1 and r <= T2:
                processed_img1[x, y] = 100
                processed_img2[x, y] = 100
            else:
                processed_img1[x, y] = 10
                processed_img1[x, y] = r

            processed_img3[x, y] = c * math.log(1 + r, 10)
            processed_img4[x, y] = c * pow(r + epsilon, p)

    img_set = [processed_img1, processed_img2, processed_img3, processed_img4]
    title_set = ['Processed-1', 'Processed-2', 'Processed-3', 'Processed-4']

    plot_img(img_set, title_set)


def plot_img(img_set, title_set):
    n = len(img_set)
    plt.figure(figsize=(20, 20))

    for i in range(n):
        plt.subplot(2, 2, i+1)
        plt.title(title_set[i])
        plt.imshow(img_set[i], cmap='gray')
    plt.savefig('Processed_Points.jpg')
    plt.show()


if __name__ == '__main__':
    main()