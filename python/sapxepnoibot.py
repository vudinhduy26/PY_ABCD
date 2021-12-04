# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:40:01 2021

@author: duy
"""

def bubble_sort(n):
    flag = True
    while flag:
        flag = False
        for i in range(len(n)-1):
            if a[i] > a[i+1]:
                a[i] , a[i+1] = a[i+1] , a[i]
                flag = True

n = int(input())
k = input().split(" ")
a = [int(i) for i in k[:n]]
bubble_sort(a)
b = []
for i in a:
    b.append(str(i))
print(' '.join(b))