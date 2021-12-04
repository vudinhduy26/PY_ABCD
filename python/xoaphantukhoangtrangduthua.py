# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:02:24 2021

@author: duy
"""
import re
n = input()
k = n.strip() # xoa phan tu trang o dau va cuoi
k = re.findall(r'[a-zA-Z0-9]\w{0,}', n)
print(' '.join(k))