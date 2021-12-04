# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 18:04:01 2021

@author: duy
"""

def UCLN(a,b):
    if b == 0:
        return a
    return UCLN(b,(a%b))

n=input().split()
k = [int(i) for i in n]
c = 0
arr = []
for i in range(len(k)):
    for j in range(i+1,len(k)):
        arr.append(UCLN(k[i],k[j]))
print(min(arr))