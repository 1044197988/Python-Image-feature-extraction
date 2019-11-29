# Python-Image-feature-extraction
Python实现提取图像的纹理、颜色特征，包含快速灰度共现矩阵（GLCM）、LBP特征、颜色矩、颜色直方图。

# 原始图片
![image](https://github.com/1044197988/Python-Image-feature-extraction/blob/master/Image/origin.png)

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
![GLCM](https://github.com/1044197988/Python-Image-feature-extraction/blob/master/Image/GLCM.png)

### LBP
获取图像的LBP特征：对图像的原始LBP模式、等价LBP模式、旋转不变LBP模式，以及等价旋转不变LBP模式的LBP特征进行提取以及显示。<br>
get_LBP_from_Image.py 主要文件 获取图像的LBP特征。<br>
get_resolve_map.py和get_uniform_map.py主要是做降维后新的像素值的映射。已经将求出的结果写入了get_LBP_from_Image.py中，这两个主要是帮助理解算法降维后新的像素值怎么得到的。
![LBP](https://github.com/1044197988/Python-Image-feature-extraction/blob/master/Image/LBP.png)
## 颜色特征
### 颜色矩
颜色是彩色图像最重要的内容之一，被广泛用于图像检索中。但从图像中提取颜色特征时，很多算法都先要对图像进行量化处理。量化处理容易导致误检，并且产生的图像特征维数较高，不利于检索。AMA Stricker和M Orengo提出了颜色矩的方法，颜色矩是一种简单有效的颜色特征表示方法，有一阶矩(均值,mean)、二阶矩(方差, variance)和三阶矩(斜度,skewness)等，由于颜色信息主要分布于低阶矩中，所以用一阶矩，二阶矩和三阶矩足以表达图像的颜色分布，颜色矩已证明可有效地表示图像中的颜色分布，该方法的优点在于：不需要颜色空间量化，特征向量维数低；但实验发现该方法的检索效率比较低，因而在实际应用中往往用来过滤图像以缩小检索范围。<br>
### 颜色直方图
![RGB-histogram](https://github.com/1044197988/Python-Image-feature-extraction/blob/master/Image/RGB-histogram.png)
![gray-histogram](https://github.com/1044197988/Python-Image-feature-extraction/blob/master/Image/gray-histogram.png)
![histogram](https://github.com/1044197988/Python-Image-feature-extraction/blob/master/Image/histogram.png)
# 参考
* [michael92ht/LBP](https://github.com/michael92ht/LBP)
* [tzm030329/GLCM](https://github.com/tzm030329/GLCM)

