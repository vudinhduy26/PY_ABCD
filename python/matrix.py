# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 10:25:37 2021

@author: duy
"""

import numpy as np
M=int(input())
matrix = []
k=2
c=M+2
for i in range(M):
    matrix.append([])
    for j in range(k,c):
        matrix[i].append(str(j))
    k+=1
    c+=1
#A = np.array(matrix)
for row in matrix:
    print(' '.join(row))