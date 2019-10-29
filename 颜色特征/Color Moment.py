from PIL import Image
import numpy as np
import os

"""
#r通道的一阶颜色矩
rd_1 = rd.mean()
 
#r通道的二阶颜色矩
rd_2 = rd.std()
"""

#定义一个求三阶颜色矩的函数
def var(x=None):
    mid = np.mean(((x - x.mean()) ** 3))
    return np.sign(mid) * abs(mid) ** (1/3)

#批量求一个文件夹下所有图片的各阶颜色矩： 
def getimagedata(path):
    filename = os.listdir(path)
    n = len(filename)
    data = np.zeros([n,9])
    for i in range(n):
        img = Image.open(path +'\\'+ filename[i])
        M,N = img.size
        r,g,b = img.split()
        rd = np.asarray(r)
        gd = np.asarray(g)
        bd = np.asarray(b)
        data[i,0] = rd.mean()
        data[i,1] = gd.mean()
        data[i,2] = bd.mean()
        data[i,3] = rd.std()
        data[i,4] = gd.std()
        data[i,5] = bd.std()
        data[i,6] = var(rd)
        data[i,7] = var(gd)
        data[i,8] = var(bd)
    return data

if __name__=='__main__':
    a = getimagedata("C:\\Users\\Admin\\Desktop\\666\\Project\\segmention\\train")
