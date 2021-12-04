# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:01:30 2021

@author: duy
"""

n,k=map(int,input().split())
keo = [1]
keoso = 1
for i in range(2,n+1):
    keoso += 3
    if keoso <k:
        keo.append(keoso)
sumsum = 0
a=0
for j in keo:
    sumsum +=j
    if sumsum <= k:
        a+=1
print(a)