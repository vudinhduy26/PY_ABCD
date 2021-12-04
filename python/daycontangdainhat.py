# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 19:22:03 2021

@author: duy
"""
a = []
b = []
ketqua = 0
for i in range(1,7):
    a.append(int(input('n : ')))
for j in range(1,7):
    b[j] = 1
    for g in range(1,j-1):
        if a[j] > a[g] and b[g] >= b[j]:
            b[j] = b[g] + 1
    if b[j] > ketqua:
        ketqua = b[j]
print(ketqua)