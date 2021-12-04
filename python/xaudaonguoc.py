# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 18:17:39 2021

@author: duy
"""

def xaudaonguoc(strr):
    if len(strr) == 1:
        return strr
    return strr[-1]+xaudaonguoc(strr[:-1])
def main():
    s=input()
    print(xaudaonguoc(s))
if __name__ == '__main__':
    main()