# Python-Image-feature-extraction
Python实现提取图像的纹理、图像特征，包含快速灰度共现矩阵（GLCM）、LBP特征、颜色矩、颜色直方图。

# 参考
* [michael92ht/LBP](https://github.com/michael92ht/LBP)
* [tzm030329/GLCM](https://github.com/tzm030329/GLCM)

# 原始图片


## 纹理特征
### GLCM
numpy的快速灰度共现矩阵（GLCM）。该脚本在没有每个像素For循环的情况下计算GLCM，并且在scikit-image上比GLCM更快地工作。
```python
import fast_glcm
from skimage import data

if __name__ == '__main__':
    img = data.camera()
    glcm_mean = fast_glcm.fast_glcm_mean(img)
```
![Tensorflow](https://github.com/1044197988/Awesome-Tensorflow2/blob/master/Logo/Logo.jpg)

### LBP
获取图像的LBP特征：对图像的原始LBP模式、等价LBP模式、旋转不变LBP模式，以及等价旋转不变LBP模式的LBP特征进行提取以及显示。<br>
get_LBP_from_Image.py 主要文件 获取图像的LBP特征。<br>
get_resolve_map.py和get_uniform_map.py主要是做降维后新的像素值的映射。已经将求出的结果写入了get_LBP_from_Image.py中，这两个主要是帮助理解算法降维后新的像素值怎么得到的。
![Tensorflow](https://github.com/1044197988/Awesome-Tensorflow2/blob/master/Logo/Logo.jpg)
## 颜色特征
### 颜色矩
![Tensorflow](https://github.com/1044197988/Awesome-Tensorflow2/blob/master/Logo/Logo.jpg)

### 颜色直方图
![Tensorflow](https://github.com/1044197988/Awesome-Tensorflow2/blob/master/Logo/Logo.jpg)
