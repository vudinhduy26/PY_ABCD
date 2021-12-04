# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 22:17:18 2021

@author: duy
"""

n,m = map(int,input().split(" "))
tiengoc = n
tiengocmoi = tiengoc + round(tiengoc*0.1)
count = 1
while m > tiengocmoi:
    tiengoc = tiengocmoi
    tiengocmoi = tiengoc + round(tiengoc*0.1)
    count = count + 1
print(count)