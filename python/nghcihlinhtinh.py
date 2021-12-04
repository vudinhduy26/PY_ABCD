# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 11:36:21 2021

@author: duy
"""

import string
import random

Letters = string.ascii_letters
number = string.digits
punctuation = string.punctuation

def password_generator(length=8):
    printable = f"{Letters}{number}{punctuation}"
    printable = list(printable)
    random.shuffle(printable)
    random_password = random.choices(printable,k=length)
    random_password = ''.join(random_password)
    return printable

def get_password_length():
    password_length = input()
    return int(password_length)
def main():
    password_length = get_password_length()
    password = password_generator()
    print(password)
    
if __name__ == "__main__":
    main()