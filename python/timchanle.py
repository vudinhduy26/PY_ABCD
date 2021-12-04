# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:50:49 2021

@author: duy
"""

n = int(input())
if 3<=n and n<=100:
    a = []
    b = []
    c = []
    str = input().split(" ")
    a = [int(x) for x in str[:n]]
    for i in a:
        if i%2 == 0:
            b.append(i)
        else:
            c.append(i)
    if len(b) < len(c):
        print(b[0])
    else:
        print(c[0])