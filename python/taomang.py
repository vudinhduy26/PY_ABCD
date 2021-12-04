# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 11:29:42 2021

@author: duy
"""
import numpy as np
def createMatrix(a,b):#a hang b cot
    z = 0
    arr = []
    while z < a:
        col = input().split()
        colint = [int(i) for i in col]
        arr.append(colint[:b])
        z+=1
    return arr

def main():
    n,m=map(int,input().split())
    count = 0
    arrays = createMatrix(n,m)
    for row in arrays:
        for i in row:
            if i%3==0:
                count+=1
    print(count)
if __name__ == "__main__":
    main()