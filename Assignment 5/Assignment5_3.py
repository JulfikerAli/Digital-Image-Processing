import matplotlib.pyplot as plt
import cv2
import numpy as np


def main():
    img_path = 'animation.jpg'
    rgb = plt.imread(img_path)
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)

    laplacian = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    img1 = cv2.filter2D(gray, -1, laplacian)

    sobel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    img2 = cv2.filter2D(gray, -1, sobel)

    plt.subplot(2, 1, 1)
    plt.title('Laplacian Filter')
    plt.imshow(img1, cmap='gray')
    plt.subplot(2, 1, 2)
    plt.title('Sobel Filter')
    plt.imshow(img2, cmap='gray')
    plt.savefig('Laplacian_Filter.jpg')
    plt.show()


if __name__ == '__main__':
    main()