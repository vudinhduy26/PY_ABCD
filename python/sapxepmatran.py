# -*- coding: utf-8 -*-
"""
Created on Mon May  3 10:33:39 2021

@author: duy
"""
def creatMatrix(n,m):
    arr = []
    while n > 0:
        k = input().split()
        ptTheoHang = [int(i) for i in k[:m]]
        arr.append(ptTheoHang)
        n-=1
    return arr
def main():
    n,m = map(int,input().split())
    maTrix = creatMatrix(n, m)
    for i in range(n):
        for j in range(m):
            for k in range(i,n):
                if k==i:
                    for l in range(j+1,m):
                        if maTrix[i][j] > maTrix[k][l]:
                            s = maTrix[i][j]
                            maTrix[i][j] = maTrix[k][l]
                            maTrix[k][l] = s
                else:
                    for l in range(1,m):
                        if maTrix[i][j] > maTrix[k][l]:
                            s = maTrix[i][j]
                            maTrix[i][j] = maTrix[k][l]
                            maTrix[k][l] = s
    print(maTrix)
if __name__ == "__main__":
    main()