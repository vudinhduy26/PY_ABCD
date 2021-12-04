# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 18:04:35 2021

@author: duy
"""

x1,v1,x2,v2 = map(int,input().split())
n = 1
flag = False
while n < 10000:
    n +=1
    if x1 == x2:
        flag = True
        break
    else:
        x1 +=v1
        x2 +=v2
if flag == True:
    print("YES")
else:
    print("NO")