# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:15:08 2021

@author: duy
"""

def MaHoa(plaintext,key):
    ciphertext=""
    for c in plaintext:
        if c!=" ":
            so = ord(c)-65
            so = (so+key)%26
            ciphertext = ciphertext+chr(so+65)
        else:
            ciphertext = ciphertext+c
    return ciphertext


k = int(input())
text = input()
print(MaHoa(text, k))