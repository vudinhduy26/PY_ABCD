# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 17:21:59 2021

@author: duy
"""
def emailProcess(email):
    #youtube
    email_username = email[0:email.index("@")]
    domain_email = email[email.index("@")+1:]
    return [email_username,domain_email]

def printMsg(email_name,email_domain):
    print(f"Username : {email_name} | Domain : {email_domain}")

def main():
    email = input().strip()
    email_name , email_domain = emailProcess(email)
    
if __name__ == "__main__":
    main()