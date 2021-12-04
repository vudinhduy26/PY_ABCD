# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 22:45:52 2021

@author: duy
"""

n = int(input())
a= [1]
b = []
tong = 0
for i in range(n-1):
    a.append(i)
for j in range(1,n):
    c = a[j-1] + 3
    a.insert(j,c)
for z in a[:n]:
    tong += z
    b.append(str(z))
print(tong)
print(' '.join(b))