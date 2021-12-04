# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 18:06:04 2021

@author: duy
"""

def childsum(arr,s):
    sum=0
    ret = []
    k=0
    i=0
    while i < len(arr):
        if sum > s:
            sum=0
            ret = []
            k+=1
            i=k
        if sum ==s:
            return ret
        if sum<s:
            sum+=arr[i]
            ret.append(arr[i])
        i+=1
    return -1
n = int(input())
z = input().split()
a = [int(i) for i in z[:n]]
s = int(input())
print(childsum(a,s))
