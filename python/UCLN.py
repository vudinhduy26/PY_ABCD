# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 16:30:40 2021

@author: duy
"""
def UCLN(n,k):
    if k==0:
        return n
    return UCLN(k,n%k)

a,b=map(int,input().split())
"""
tmp = 0
while b > 0:
    a = a%b
    tmp = a
    a = b
    b = tmp
"""
print(UCLN(a,b))