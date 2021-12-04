# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 08:45:50 2021

@author: duy
"""
import numpy as np
def creatMatrix(a,b):
    arr = []
    tang = 0
    while tang < a:
        column = input().split()
        columnInt = [int(i) for i in column]
        arr.append(columnInt[:b])
        tang+=1
    return arr
def main():
    m,n=map(int,input().split())
    Matrix = np.array(creatMatrix(m,n))
    Matrix1 = sorted(Matrix.reshape(-1))
    Matrix2 = []
    for i in Matrix1:
        Matrix2.append(str(i))
    Matrix3 = np.array(Matrix2)
    for row in Matrix3.reshape(m,n):
        print(' '.join(row))
if __name__ == "__main__":
    main()