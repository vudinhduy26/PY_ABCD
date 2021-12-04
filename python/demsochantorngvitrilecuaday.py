# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 18:58:13 2021
if a[i] % 2 == 0 and i % 2 == 0:
        sum = sum + a[i]
@author: duy
"""
n = int(input())
k = input().split()
sum = 0
b = [0]
a = [int(i) for i in k[:n]]
for i in a:
    b.append(i)
c = b[1::2]
for i in c:
    if i % 2 == 0:
        sum = sum + i
print(sum)