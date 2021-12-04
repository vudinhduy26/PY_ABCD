# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 11:12:11 2021

@author: duy
"""
import math
def snsnt(n):
    note =  [True]*(n+1)
    can_n = round(math.sqrt(n))+1
    for i in range(2,can_n+1):
        if note[i]:
            for j in range(i*i,n+1,i):
                note[j] = False

    a = []
    for i in range(2,n+1):
        if note[i]:
            a.append(i)
    return a
n = 2000000
b = snsnt(n)
c = []
T = int(input())
count = 0
while T > count:
    N = int(input())
    c.append(N)
    count += 1
for i in c:
    print(b[i-1])
