# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:36:21 2021

@author: duy
"""
import re
f = open('Document.txt','r')
str = f.read()
d = {}
k = re.findall(r'[a-zA-Z]\w{1,}', str)
for i in k:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)