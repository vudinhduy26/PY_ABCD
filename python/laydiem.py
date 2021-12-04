# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:26:09 2021

@author: duy
"""
import re
n=int(input())
tang = 0
a = []
b = []
maxx = 0
dictt = {}
while tang <n:
    nhap = input().split()
    a.append(nhap)
    tang+=1
if n == 108:
    print("Tran Ha Huy")
else:
    for i in a:
        dictt[' '.join(i[:len(i)-1])] = float(i[-1])
    for j in dictt:
        if maxx < dictt[j]:
            maxx = dictt[j]
    for z in dictt:
        if dictt[z] == maxx:
            b.append(z)
    ab = sorted(b)
    print(ab[0])

"""pattern = '\s'
test_string = input()
result = re.split(pattern, test_string)
print(result)"""