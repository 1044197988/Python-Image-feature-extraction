# -*- coding: utf-8 -*-
    # get_resolve_map.py
    # 2015-7-7
    # github: https://github.com/michael92ht
    #__author__ = 'huangtao'

#求为旋转不变模式的36种特征值从小到大进行序列化编号得到的字典

import string

#对一个二进制表示旋转一周取最小值
def get_min_for_revolve(arr,values):
    h=[]
    circle=arr
    circle.extend(arr)
    for i in range(0,8):
        j=0
        sum=0
        bit_num=0
        while j<8:
            sum+=circle[i+j]<<bit_num
            bit_num+=1
            j+=1
        h.append(sum)
    values.append(min(h))
    
if __name__ == '__main__':
    
    values=[]
    for i in range(0,256):  #分别求出0~255的二进制表示旋转一周后的最小值
        b=bin(i)
        length=len(b)
        arr=[]
        j=length-1
        while(j>1):             #构造二进制表示的列表
            arr.append(string.atoi(b[j]))
            j-=1
        for s in range(0,8-len(arr)):
            arr.append(0)
        get_min_for_revolve(arr,values)
        
    values.sort()           #构造字典
    map={}
    num=0
    f=open(r"d:/cv/test.txt",'w')
    for v in values:
        if not map.has_key(v):
            map[v]=num
            num+=1
            f.write(str(v)+':'+str(map[v])+',')



        
        
