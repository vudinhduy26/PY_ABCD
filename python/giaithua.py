# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:18:18 2021

@author: duy
"""

def giaithua(h):
    if h == 1:
        return 1
    else:
        return giaithua(h-1)*h

n = int(input())
s = 0
if n == 1:
    print("1.0000000000")
elif n == 2:
    print("1.5000000000")
else:
    for i in range(1,n+1):
        s += 1/giaithua(i)
    print(round(s,10))