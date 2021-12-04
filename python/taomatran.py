# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 03:25:42 2021

@author: duy
"""
import numpy as np
def main():
    n=int(input())
    a=2
    b=n+2
    arr = [[] for i in range(n)]
    for row in arr:
        for col in range(a,b):
            row.append(str(col))
        a+=1
        b+=1
    maTrix = np.array(arr)
    print(np.shape(maTrix))
if __name__ == "__main__":
    main()