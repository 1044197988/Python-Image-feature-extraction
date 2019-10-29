# coding: utf-8

import numpy as np
from skimage import data
from matplotlib import pyplot as plt
import fast_glcm
from PIL import Image

def main():
    pass


if __name__ == '__main__':
    #main()
    image = r"C:\\Users\\Admin\\Desktop\\666\\Project\\segmention\\train\\4_3_0.tif";
    img=np.array(Image.open(image).convert('L'))
    #img = data.camera()
    h,w = img.shape

    mean = fast_glcm.fast_glcm_mean(img)
    std = fast_glcm.fast_glcm_std(img)
    cont = fast_glcm.fast_glcm_contrast(img)
    diss = fast_glcm.fast_glcm_dissimilarity(img)
    homo = fast_glcm.fast_glcm_homogeneity(img)
    asm, ene = fast_glcm.fast_glcm_ASM(img)
    ma = fast_glcm.fast_glcm_max(img)
    ent = fast_glcm.fast_glcm_entropy(img)

    plt.figure(figsize=(10,4.5))
    fs = 15
    plt.subplot(2,5,1)
    plt.tick_params(labelbottom=False, labelleft=False)
    plt.imshow(img)
    plt.title('original', fontsize=fs)

    plt.subplot(2,5,2)
    plt.tick_params(labelbottom=False, labelleft=False)
    plt.imshow(mean)
    plt.title('mean', fontsize=fs)

    plt.subplot(2,5,3)
    plt.tick_params(labelbottom=False, labelleft=False)
    plt.imshow(std)
    plt.title('std', fontsize=fs)

    plt.subplot(2,5,4)
    plt.tick_params(labelbottom=False, labelleft=False)
    plt.imshow(cont)
    plt.title('contrast', fontsize=fs)

    plt.subplot(2,5,5)
    plt.tick_params(labelbottom=False, labelleft=False)
    plt.imshow(diss)
    plt.title('dissimilarity', fontsize=fs)

    plt.subplot(2,5,6)
    plt.tick_params(labelbottom=False, labelleft=False)
    plt.imshow(homo)
    plt.title('homogeneity', fontsize=fs)

    plt.subplot(2,5,7)
    plt.tick_params(labelbottom=False, labelleft=False)
    plt.imshow(asm)
    plt.title('ASM', fontsize=fs)

    plt.subplot(2,5,8)
    plt.tick_params(labelbottom=False, labelleft=False)
    plt.imshow(ene)
    plt.title('energy', fontsize=fs)

    plt.subplot(2,5,9)
    plt.tick_params(labelbottom=False, labelleft=False)
    plt.imshow(ma)
    plt.title('max', fontsize=fs)

    plt.subplot(2,5,10)
    plt.tick_params(labelbottom=False, labelleft=False)
    plt.imshow(ent)
    plt.title('entropy', fontsize=fs)

    plt.tight_layout(pad=0.5)
    plt.savefig('img/output.jpg')
    plt.show()
