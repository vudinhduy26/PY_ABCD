# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:43:01 2021

@author: duy
"""

n = int(input())
a = input().split()
k = [int(i) for i in a[:n]]
c = []
aa = 0
bb = 0
for i in range(len(k)):
    if k[i] == max(k):
        aa = i
    elif k[i] == min(k):
        bb = i
tg = k[aa]
k[aa] = k[bb]
k[bb] = tg
for j in k:
    c.append(str(j))
print(' '.join(c))