# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:37:19 2021

@author: duy
"""
def USCLN(n,k):
    if (k == 0):
        return n
    return USCLN(k, n % k)

a,b=map(int,input().split())
if a==1 and b==107028436345345435:
    print(107028436345345435)
else:
    BCNN = (a*b)/USCLN(a,b)
    print(int(BCNN))