# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 07:51:42 2021

@author: duy
"""

def snt(n):
    lucdau = [True]*(n+1) #gia su ban dau de la snt
    can_n = int(n**0.5)+1
    for i in range(2,can_n):
        if lucdau[i]:
            for j in range(i*i,n+1,i):
                lucdau[j] = False
    a = []
    for i in range(2,n+1):
        if lucdau[i]:
            a.append(i)
    return a

sn = int(input())
print(snt(sn))
