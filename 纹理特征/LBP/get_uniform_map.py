# -*- coding: utf-8 -*-
    # get_uniform_map.py
    # 2015-7-7
    # github: https://github.com/michael92ht
    #__author__ = 'huangtao'

#求等价模式的58种特征值从小到大进行序列化编号得到的字典

#求其二进制表示旋转一周的8个值
def circle(arr,values):
    for i in range(0,8):
        b=0
        sum=0
        for j in range(i,8):
            sum+=arr[j]<<b
            b+=1
        for k in range(0,i):
            sum+=arr[k]<<b
            b+=1
        values.append(sum)
#等价模式的特征二进制表示中1都是连续出现的，模拟连续出现1~7个1，然后求其旋转一周的8个值
def get_from():
    f=open(r"d:/cv/test.txt",'w')
    values=[]
    for i in range(1,8):
        init_value=0
        init_length=8
        arr=[init_value]*init_length
        j=0
        while(j<i):
            arr[j]=1
            j+=1
        circle(arr,values)    
    values.sort()
    num=1
    map={}
    for v in values:
        map[v]=num
        num+=1
        f.write(str(v)+':'+str(map[v])+',')
       

if __name__ == '__main__':
    get_from()      
