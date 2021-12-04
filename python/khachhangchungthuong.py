# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 19:23:13 2021

@author: duy
"""

n = int(input())
k = input().split()
khachhang = [int(i) for i in k[:n]]
nguoitrung = int(input())
b = [0]
for i in khachhang:
    b.append(i)
for i in range(1,n+1):
    if b[i] == nguoitrung:
        print(i)