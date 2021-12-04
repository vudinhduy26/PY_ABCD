# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:12:22 2021

@author: duy
"""
def strs(arr):
    STR = []
    for i in arr:
        STR.append(str(i))
    return " ".join(STR)

N,K = map(int,input().split()) #N la so ptu cua mang , K la so can tim
strr = input().split()
A = [int(i) for i in strr[:N]]
B = []
dem = 0
flag = 0
for i in range(len(A)):
    if A[i] == K:
        dem +=1
        B.append(i+1)
        flag = A[i]
if flag == K:
    print(dem)
    print(strs(B))
else:
    print("NO")