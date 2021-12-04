# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 04:26:04 2021

@author: duy
"""

def creatMatrix(m,n):
    arr = []
    while m > 0:
        pT = input().split()
        hang = [int(i) for i in pT[:n]]
        arr.append(hang)
        m-=1
    return arr
def main():
    m,n=map(int,input().split())
    maTrix = creatMatrix(m, n)
    S = 0
    t = 0
    arrSum =[]
    """
    while t < n:
        for row in range(len(maTrix)):
            S += maTrix[row][t]
        print(S)
        S = 0
        t+=1"""
    for i in range(n):
        for row in range(len(maTrix)):
            S += maTrix[row][i]
        print(S)
        S = 0
if __name__ == "__main__":
    main()