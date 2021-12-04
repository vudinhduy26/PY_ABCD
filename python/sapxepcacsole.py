# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:13:58 2021

@author: duy
"""
a = [1,8,3,9,2,0,5]
for i in range(len(a)):
    for j in range(i):
        if a[i]<a[j] and a[i]%2!=0 and a[j]%2!=0:
            b=a[j]
            a[j]=a[i]
            a[i]=b
print(a)