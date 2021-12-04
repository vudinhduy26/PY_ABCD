# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 22:56:12 2021

@author: duy
"""

class MonHoc():
    #phuong thuc khoi tao vs cac tham so
    def __init__(self,maMH = '',tenMH='',soTC=0):
        self.maMH = maMH
        self.tenMH = tenMH
        self.soTC = soTC
    #hien thi thong tin mon hoc ra man hinh
    def hienThiMH(self):
        print(self.maMH,self.tenMH,self.soTC,self.diem)
    #nhap thong tin tu ban phim
    def nhapMH(self):
        while True:
            self.maMH = input('Nhap ma mon hoc : ')
            if self.maMH != '':
                break
        while True:
            self.tenMH = input('Nhap ten mon hoc : ')
            if self.tenMH != '':
                break
        while True:
            self.soTC = int(input('So tin chi : '))
            if self.soTC > 0 and self.soTC <= 4:
                break
    def toString(self):
        return '#*'.join([self.maMH,self.tenMH,str(self.soTC)])
###
class quanlyMH():
    def __init__(self,file_path):
        self.danh_sach_MH = list()
        self.file_path = file_path
    #do thong tin cac mon hoc tu file
    def read_MH_from_file(self):
        file = open(self.file_path,'r',encoding='utf-8')
        lines_MH = file.readlines()
        file.close()
        self.danh_sach_MH = list()
        for mh in lines_MH:
            tmp = mh.split('#*')
            if len(tmp) == 3:
                mon_hoc = MonHoc(tmp[0],tmp[1],tmp[2])
                self.danhsachMH.append(mon_hoc)
    #ghi thong tin mon hoc vao file
    def write2File(self):
        file = open(self.file_path,'w',encoding='utf-8')
        for i in range(len(self.danh_sach_MH)-1):
            file.write(self.danh_sach_MH[i].toString())
            file.write('\n')
        if len(self.danh_sach_MH) >= 1:
            file.write(self.danh_sach_MH[-1].toString())
        file.close()
    #them mot mon hoc moi
    def themmotmonhocMoi(self):
        mh = MonHoc()
        mh.nhapMH()
        self.danh_sach_MH.append(mh)
        file = open(self.file_path,'a',encoding='utf-8')
        file.write('\n'+mh.toString()) #ghi vao cuoi file
        file.close()
    #hien thi cac mon hoc ra man hinh
    def hienthimonHoc(self):
        print('STT  Ma Mon Hoc  Ten Mon Hoc  So tin chi')
        for(i,mh) in enumerate(self.danh_sach_MH):
            print('  '.join([str(i+1),mh.maMH,mh.tenMH,str(mh.soTC)]))
    #xoa mon hoc co ma la maMH
    def xoaMH(self,maMH):
        xoa = 0
        for (i,mh) in enumerate(self.danh_sach_MH):
            if mh.maMH == maMH:
                self.danh_sach_MH.remove(mh)
                xoa = 1
        #delete mh so to update file
        if xoa == 1:
            self.write2File()
    #show into screen the subject , these satisfy information find
    def tim_MH(self,ma='',ten='',soTC=0):
        print('STT  Ma Mon Hoc  Ten Mon Hoc  So tin chi')
        sl = 0
        for (i,mh) in enumerate(self.danh_sach_MH):
            if mh.maMH.lower().__contains__(ma.lower()) and mh.tenMH.lower().__contains__(ten.lower()) and soTC == 0 or soTC > 0 and mh.soTC == soTC:
                sl = sl + 1
                print('  '.join([str(sl),mh.maMH,mh.tenMH,str(mh.soTC)]))
            if sl == 0:
                print('ko co mon hoc')
#chinh
qlmonhoc = quanlyMH('monhoc.txt')
qlmonhoc.read_MH_from_file()
qlmonhoc.themmotmonhocMoi()
print('Danh sach mon hoc')
qlmonhoc.hienthimonHoc()
print('danh sach mh co ma m01')
qlmonhoc.tim_MH(ma='mh01')