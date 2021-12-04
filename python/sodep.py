# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:53:52 2021

@author: duy
"""

n=input()
a = [int(i) for i in n]
sum = 0
for i in a:
    sum +=i
b = 9
flag = False
while b <= sum:
    if sum == b:
        flag = True
    b +=10
if flag == True:
    print("YES")
else:
    print("NO")