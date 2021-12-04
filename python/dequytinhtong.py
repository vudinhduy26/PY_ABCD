# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 09:44:22 2021

@author: duy
"""

def tong(n):
    if not n:
        return 0
    return n[0]+tong(n[1:])

z = input()
a = [int(i) for i in z]
print(tong(a))
