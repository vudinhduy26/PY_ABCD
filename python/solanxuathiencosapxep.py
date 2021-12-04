# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:30:20 2021

@author: duy
"""

n = input("")
d = {}
for i in n:
    if i != " ":
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
for i in sorted(d):
    print(i,d[i])