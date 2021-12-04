# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 20:40:40 2021

@author: duy
"""

#import math
#n , m = map(float, input().split()) 
#count = 0
#while n < m:
 #   n = n + round(n*10/100)
 #   count += 1
#print(count)

#####
mod = 123456789
def pow2(n,k):
    if k == 1:
        return n
    st = pow2(n,k // 2)
    print('.a',st)
    if k % 2 == 0:
        return st * st % mod
    else:
        return (st * st % mod) * n % mod
 
n = int(input())
print(pow2(2,n - 1))

np = 5%mod
print(np)