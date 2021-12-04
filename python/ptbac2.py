# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 23:10:41 2021

@author: duy
"""
import math
a,b,c=map(int,input().split())
denta=(b**2)-(4*a*c)
x1 = 0
x2 = 0
if denta >0:
    x1 = (-b+math.sqrt(denta))/(2*a)
    x2 = (-b-math.sqrt(denta))/(2*a)
    print("PT CO HAI NGHIEM")
    print("X1 =","{0:.2f}".format(x1))
    print("X2 =","{0:.2f}".format(x2))
elif denta==0:
    x1=x2=-b/(2*a)
    print("PT CO NGHIEM KEP")
    print("X =","{0:.2f}".format(x1))
elif denta<0:
    print("VO NGHIEM")