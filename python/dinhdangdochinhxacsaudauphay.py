# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:53:32 2021

@author: duy
"""
n = float(input())
e = 0
z = 1
while e < n:
    e += 1/(z**2)
    z += 1
print("{0:.9f}".format(e)) #dinh dang do chinh xac sau dau phay