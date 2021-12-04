# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 09:05:58 2021

@author: duy
"""

n = int(input())
k = input().split()
a = [int(i) for i in k[:n]]
count = 0
for i in range(len(a)):
    if a[i] == a[0]:
        count += 1
    else:
        count += -1
print(abs(count))