import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    img_path = 'animation.jpg'
    image = plt.imread(img_path)

    grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    grayscale_histogram = cv2.calcHist([grayscale], [0], None, [256], [0, 256])

    grayscale_equalization = cv2.equalizeHist(grayscale)
    grayscale_equalized_histogram = cv2.calcHist([grayscale_equalization], [0], None, [256], [0, 256])
    
    img_set = [grayscale, grayscale_histogram, grayscale_equalization, grayscale_equalized_histogram ]
    title_set = ['Original','Grayscale Histogram','Grayscale Equalization', 'Histogram Equalization']

    plot_images(img_set, title_set)
    
def equHist(grayscale):
    values, counts = np.unique(grayscale, return_counts=True)

    prob_values = counts / sum(counts)
    cm = np.cumsum(prob_values)
    l = grayscale.max() * cm
    l = np.round(l)
    print(list(zip(values, counts, l)))


def equHist2(grayscale):
    values, counts = np.unique(grayscale, return_counts=True)
    cum_counts = np.cumsum(counts)

    cum_counts_norm = cum_counts / cum_counts[-1]
    cum_counts_norm_mul_by_max = cum_counts_norm * grayscale.max()

    cum_counts_round = np.round(cum_counts_norm_mul_by_max)

    print(list(zip(values, counts, cum_counts_round)))


def plot_images(img_set, img_title):
    for i in range(len(img_set)):
        plt.subplot(2, 2, i + 1)
        plt.title(img_title[i])

        if img_set[i].shape[1] == 1:
            plt.plot(img_set[i])
        else:
            plt.imshow(img_set[i], cmap="gray")

    plt.savefig('Histogram Equalization.png')
    plt.show()

if __name__ == '__main__':
	main()
 
img_path = "animation.jpg"
image = plt.imread(img_path)

grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
grayscale_histogram = cv2.calcHist([grayscale], [0], None, [256], [0, 256])

grayscale_equalization = cv2.equalizeHist(grayscale)
grayscale_equalized_histogram = cv2.calcHist([grayscale_equalization], [0], None, [256], [0, 256])

img_set = [grayscale, grayscale_histogram, grayscale_equalization, grayscale_equalized_histogram]
img_title = ['Original','Grayscale Histogram','Grayscale Equalization', 'Histogram Equalization']

plot_images(img_set, img_title)