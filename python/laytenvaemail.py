# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 17:35:34 2021

@author: duy
"""

from codex import emailProcess,printMsg

def main():
    f = open('email.txt','r')
    email = f.read().split('\n')
    for i in email:
       email_name , email_domain = emailProcess(i)
       printMsg(email_name , email_domain)


if __name__ == "__main__":
    main()