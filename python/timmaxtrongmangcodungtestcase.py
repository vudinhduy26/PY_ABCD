# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 16:25:35 2021

@author: duy
"""
def largest(arr,n):
    maxx=0
    for i in arr[:n]:
        if i > maxx:
            maxx = i
    return maxx
def main():
    T = int(input())
    while T>0:
        n=int(input())
        arr= [int(x) for x in input().strip().split()]
        print(largest(arr, n))
        T -=1
if __name__ == "__main__":
    main()