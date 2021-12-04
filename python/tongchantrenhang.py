# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 05:30:09 2021

@author: duy
"""

def creatMatrix(n):
    arr = []
    t = 0
    while t < n:
        pT = input().split()
        pTs = [int(i) for i in pT[:n]]
        arr.append(pTs)
        t+=1
    return arr
def main():
    n=int(input())
    S = 0
    maTrix = creatMatrix(n)
    """
    for row in range(len(maTrix)):
        for col in range(len(maTrix[row])):
            if maTrix[row][col] %2 == 0:
                S+=maTrix[row][col]
        print(S)
        S = 0"""
    row = 0
    while row < len(maTrix):
        for col in range(len(maTrix[row])):
            if maTrix[row][col] %2 == 0:
                S+=maTrix[row][col]
        print(S)
        S = 0
        row+=1
if __name__ == "__main__":
    main()