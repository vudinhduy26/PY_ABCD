# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 23:25:37 2021

@author: duy
"""

t=input().split()
a = [int(i) for i in t]
c = 0
for i in a:
    c +=i
print("{0:.2f}".format(c/len(a)))
