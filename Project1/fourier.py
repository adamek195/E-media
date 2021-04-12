import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


class Fourier:

    @staticmethod
    def show_plots(path):
        plt.figure(figsize=(10, 8))
        image = Image.open(path)
        image_1 = np.array(image.convert('L'))

        image_2 = np.fft.fft2(image_1)
        image_3 = np.fft.fftshift(image_2)
        image_4 = np.fft.ifft2(image_2)

        plt.subplot(221), plt.imshow(image_1, "gray"), plt.title("Image")
        plt.subplot(222), plt.imshow(20*np.log(1+np.abs(image_2)),
                                                "gray"), plt.title("Spectrum")
        plt.subplot(223), plt.imshow(20*np.log(1+np.abs(image_3)), 
                                                "gray"), plt.title("Centered")
        plt.subplot(224), plt.imshow(np.angle(image_4), 
                                                    "gray"), plt.title("Phase")
        plt.show()
