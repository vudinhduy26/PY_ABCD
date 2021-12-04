# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:55:42 2021

@author: duy
"""
def catalan(n):
    x = 1
    y = 1
    z = 1
    if n < 0:
        exit(n)
    for i in range(1,n+1):
        z *= i
    for j in range(1,2*n+1):
        x *= j
    for o in range(1,n+1+1):
        y *= o
    return(x/(y*z))
number = int(input('n : '))
print(catalan(number))

