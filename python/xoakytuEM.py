# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 08:32:54 2021

@author: duy
"""

stra = input()
check = "em"
for i in check:
    stra = stra.replace(check,'')
b = stra.replace("em",'')
print(b.replace("em",""))