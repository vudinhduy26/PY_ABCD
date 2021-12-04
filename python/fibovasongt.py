# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:42:48 2021

@author: duy
"""
import math
a , b = map(int,input("").split(" "))
dem = 0
if 0<a<b and b<10**15:
    for i in range(a,b+1):
        p = True
        if i == 1 :
            p = False
        for j in range(2,round(math.sqrt(i))+1):
            if i%j == 0:
                p = False
        if p:
            dem += 1
print(dem)