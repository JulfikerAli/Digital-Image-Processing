import matplotlib.pyplot as plt
import numpy as np
import cv2

img_path = 'animation.jpg'
rgb = plt.imread(img_path)
gray =  cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)

image_in_frequency_domain = np.fft.fft2(gray)
centered_f_img = np.fft.fftshift(image_in_frequency_domain)
magnitude_spectrum = 100 * np.log(np.abs(image_in_frequency_domain))
centered_magnitude_spectrum = 100 * np.log(np.abs(centered_f_img))
    

r , c = gray.shape
shell_image = np.ones((r,c),dtype=np.uint8)
filter = cv2.line(shell_image,(0,int(r/2)),(c,int(r/2)),(0,0,0),9)
filter_applied_f_img = centered_f_img * filter
filtered_img = np.abs(np.fft.ifft2(filter_applied_f_img))
    
plt.subplot(1,1,1)
plt.title('FFT')
plt.imshow(image_in_frequency_domain,cmap='gray')

plt.savefig('FFT.jpg')
plt.show()
