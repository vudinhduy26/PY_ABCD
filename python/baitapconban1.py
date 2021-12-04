# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 23:56:57 2021

@author: duy
"""

###so tien ban co
#X = float(input('Nhap : '))
### 
#tiengoc = X
###
#laisuat = 0.6/100 #lai suat theo thang
#Tienlai = 6*X*laisuat

#tiengoc = tiengoc + Tienlai

### 6 thang tiep theo
#Tienlai6tt = laisuat*tiengoc*6
#tiengoc6tt = Tienlai6tt + tiengoc
### 6 thang cuoi
#Tienlai6tc = laisuat*tiengoc6tt*6
#tiengoc6tc = Tienlai6tc + tiengoc6tt

#print('sau 18t A co so tien la : ',tiengoc6tc)

#####bai2
##_a = HoTen.strip()
#b = _a.title()
#s = b.split()
#print(s)
#s1 =" ".join(s)
#print(s1)

#x = (10+2*7)/3
#print('\t'.join(['LT','Python co ban',3.6]))

######bai3
#f = float(input('Nhap : '))
#c = (f-32)/1.8
#print('Nhiet do C : ',c,'.C')

######bai4
#HoTen = input('Nhap : ')
#VietHoaChuDau = HoTen.title()
#Listt = VietHoaChuDau.split()
#TenHoanChinh = " ".join(Listt)
#ListTieng = TenHoanChinh.split()
#print('Ho va Ten day du la : ',TenHoanChinh)
#print('So tieng cau tao len tu la : ',len(ListTieng))

######bai5
#R = float(input('Nhap ban kinh : '))
#pi = 3.14
#dien tich
#S = 4*pi*R**2
##the tich
#V = (4/3)*pi*R**3
#print('Dien tich la : ',S)
#print('The tich la : ',V)
#Ss = "abcd xyz"
#s2 = Ss[ : :-1] #cho buoc nhanh nhay lui
#print(s2)

####bai6
#s1 = input('Nhap chuoi 1 : ')
#s2 = input('Nhap chuoi 2 la : ')
#n = s1.find(s2)
#print(n)

######bai7
#s = input("Nhap chuoi : ")
#c = input("Nhap ki tu : ")
#countt = s.count(c)
#print('Dem : ',c,': ',countt)

######bai8
#cmt = int(input("Nhap : "))
#print('a= %d'%(cmt))

######while : vong lap ko biet truoc so lan lap
while True:
    try :
        thang = int(input('Nhap thang : '))
        if thang < 1 or thang >12:
            print('month not to be : ',thang)
        else:
            if thang >= 1 and thang <=3:
                    print('This is Spring : ',thang)
            elif thang >= 4 and thang <= 6:
                    print('This is Summer : ',thang)
            elif thang >= 7 and thang <= 9:
                    print('This is Autumn : ',thang)
            elif thang >= 10 and thang <= 12:
                    print('This is Winter :',thang)
            break
    except:
        print('Please enter month')