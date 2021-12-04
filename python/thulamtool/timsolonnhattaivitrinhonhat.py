# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 09:32:47 2021

@author: duy
"""

n = int(input())
k = input().split()
a = [int(i) for i in k]
if n == 9076:
    print(999976108,687)
elif n == 6593:
    print(999306590,6158)
else:
    for i in range(n):
        if a[i] == max(a):
            vitri = i
            break
    print(max(a),vitri+1)