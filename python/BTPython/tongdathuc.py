# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 09:33:41 2021

@author: duy
"""

def nhapdt():
    pol = dict()
    while True:
        while True:
            mu = int(input('Nhap so mu -1 de ket thuc : '))
            if mu == -1:
                break;
        heso =float(input('Nhap he so cua x^' +str(mu)+' : '))
        if heso != 0:
            pol[mu] = heso
    return pol

def hienthidt(pol):
    strpol = ''
    for pow in sorted(pol.keys()):
        if pol[pow] > 0:
            strpol = strpol + ' + ' + str(pol[pow]) + ' * x^'+str(pow)
        else:
            strpol = strpol +' '+ str(pol[pow]) +' * x^'+ str(pow)
    print('P = ',strpol.strip(' +').split())
#tinh tong 2 da thuc
def tongdt(pol1,pol2):
    pol = dict()
    for key in pol1:
        if key in pol2:
            pol[key] = pol1[key] + pol2[key]
        else:
            pol[key] = pol1[key]
    for key in pol2:
        if key not in pol1:
            pol[key] = pol2[key]
    return pol
#tinh gia tri cua da thuc tai x0
def giatridathuc(pol,x0):
    return sum(pol[pow]*x0**pow for pow in pol)

#-------------------------------------------------------
print('nhap da thuc 1')
pol1 = nhapdt()
print('nhap da thuc 2')
pol2 = nhapdt()

pol = tongdt(pol1, pol2)
x =10
#hien thi da thu
print('da thuc 1 : ')
hienthidt(pol1)
print('da thuc 2 : ')
hienthidt(pol2)
print('da thuc tong : ')
hienthidt(pol)
#hie thi gia tri da thuc tai x0
print('gai tri da thuc 1 : ')
print(giatridathuc(pol1, x))
print('gia tri da thuc 2 : ')
print(giatridathuc(pol2,x))
print('gia tri da thuc tong : ')
print(giatridathuc(pol, x))