# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 16:08:34 2021

@author: duy
"""

n=int(input())
a = input().split()
b = input().split()
#Arrs = [int(i) for i in a]
#Brrs = [int(i) for i in b]
"""for h in a:
    Arrs.append(int(h))
for hh in b:
    Brrs.append(int(hh))"""
Crr = [0]*n*2
Crr[::2]=a
Crr[1::2]=b
print(' '.join(Crr))