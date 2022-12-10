import matplotlib.pyplot as plt
import numpy as np
import cv2

def gaussian_filter(spatial_domain):
    m = spatial_domain.shape[0]
    n = spatial_domain.shape[1]
    gauss = np.zeros((m,n),dtype=np.float32)
    d0 = 10
    for u in range(m):
        for v in range(n):
            D = np.sqrt((u - m/2) ** 2 + (v - n/2) ** 2)
            gauss[u][v] = np.exp((-D**2) / (2*d0*d0))
    return gauss
    
def main():
    img_path = 'animation.jpg'
    rgb = plt.imread(img_path)
    
    # create fft of image
    gray_image = cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    fft_image = np.fft.fft2(gray_image)
    # sort the image
    sorted_image = np.sort(np.abs(fft_image.ravel()))
    n = len(sorted_image)

    #filteringlow-frequency components keeping 75% of data of the image
    threshold = sorted_image[int(np.floor(n * (1 - 0.1)))]
    allow_pass = np.where(abs(fft_image)>threshold,fft_image,0)

    #transforming back to the  spatial domain
    ifftImg = np.fft.ifft2(allow_pass).real
    
    plt.subplot(1,1,1)
    plt.title('Remaining 75%')
    plt.imshow(ifftImg,cmap='gray')

    plt.savefig('FFT11.jpg')
    plt.show()
        
    
if __name__ == '__main__':
    main()