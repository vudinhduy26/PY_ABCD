# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 19:54:18 2021

@author: duy
"""
import numpy as np
a = []
m,n = map(int,input("nhap : ").split(" "))

for i in range(0, m+1):
    a.append([]) #sinh ra hàng
    for j in range(0, n+1):
        x = (j-1)*m + i
        a[i].append(x)
print(a)

for i in range(0, m):
    for j in range(0, n):
        print("%3d " % a[i][j], end='')
    print()