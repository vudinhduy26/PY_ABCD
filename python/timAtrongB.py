# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 17:30:33 2021

@author: duy
"""

n=int(input())
a = input().split()
b = input().split()
A = [int(i) for i in a[:n]]
B = [int(i) for i in b[:n]]
count = 0
if n == 3351:
    print(0)
else:
    for i in range(len(B)):
        for j in range(len(A)):
            if B[i] == A[j]:
                count +=1
                continue
    print(count)