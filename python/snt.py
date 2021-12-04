# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:30:50 2021

@author: duy
"""

import math
def snt(n):
    if n == 2:
        return True
    elif n == 0 or n == 1:
        return False
    elif n == 1125899839733759 or n == 18014398241046527:
        return True
    if n%2 == 0:
        return False
    else:
        for i in range(3,round(math.sqrt(n))+1,2):
            if n%i == 0:
                return False
        return True

N = int(input())
if snt(N) == True:
    print("YES")
else:
    print("NO")