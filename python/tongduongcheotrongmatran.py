# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:50:01 2021

@author: duy
"""

def createMatrix(a):
    arr = []
    tang = 0
    while tang < a:
        colum = input().split()
        columInt = [int(i) for i in colum]
        arr.append(columInt[:a])
        tang+=1
    return arr
def main():
    n=int(input())
    S = 0
    Matrix = createMatrix(n)
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            if i == j:
                S += Matrix[i][j]
    print(S)
if __name__ == "__main__":
    main()