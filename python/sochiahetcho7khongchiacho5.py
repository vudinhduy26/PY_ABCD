# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:35:17 2021

@author: duy
"""
j=[]
for i in range(2000,3200):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))
print(','.join(j))