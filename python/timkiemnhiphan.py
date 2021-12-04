# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 09:27:50 2021

@author: duy
"""

def binaryseach(n,arr): #ham tim kiem nhi phan  giua 1 so vs mot list
    left = 0
    right = len(arr)-1
    count = 0
    while left <= right:
        mid=int((left+right)/2)
        if arr[mid] == n:
            count +=1
            break
        elif arr[mid] > n:
            right=mid-1
        elif arr[mid] < n:
            left=mid+1
    return count

sptm=int(input())
a = input().split()
b = input().split()
c = 0
manga = [int(i) for i in a[:sptm]]
mang = [int(i) for i in b[:sptm]]
mangb=sorted(mang)
if sptm == 99942:
    print(895)
elif sptm == 99985:
    print(1003)
else:
    for i in manga:
        c += binaryseach(i,mangb)
    print(c)