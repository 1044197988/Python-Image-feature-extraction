# coding: utf-8

import numpy as np
from skimage import data
from matplotlib import pyplot as plt
import fast_glcm

def main():
    pass


if __name__ == '__main__':
    main()

    img = data.camera()
    h,w = img.shape
    glcm_mean = fast_glcm.fast_glcm_mean(img)

    plt.imshow(glcm_mean)
    plt.tight_layout()
    plt.show()
