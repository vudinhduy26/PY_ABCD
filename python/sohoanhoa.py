# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 23:25:04 2021

@author: duy
"""
p = input()
n = int(p)
tonguoc = 0
for i in range(1,n):
    if n%i == 0:
        tonguoc += i
if tonguoc == n:
    print("YES")
else:
    print("NO")