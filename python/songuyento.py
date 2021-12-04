# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 18:11:39 2021

@author: duy
"""

import math
def songuyento(arrr):
    br=[]
    for i in arrr:
        flag=True
        for j in range(2,round(math.sqrt(i))+1):
            if i%j==0:
                flag=False
        if flag:
            br.append(i)
    return br

def main():
    a,b=map(int,input().split())
    arr = []
    for i in range(a,b+1):
        arr.append(i)
    print(songuyento(arr))
    
if __name__ == "__main__":
    main()