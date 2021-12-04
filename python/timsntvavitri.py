# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 10:56:45 2021

@author: duy
"""
import math
def snt(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,round(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
            
n = int(input())
k = input().split()
a = [int(i) for i in k[:n]]
b = {}
c = {}
for j in range(len(a)):
    if snt(a[j]) == True:
        b[j] = a[j]
if b == c:
    print("KHONG CO SO NGUYEN TO")
else:
    for i in sorted(b):
        print(i+1,b[i])