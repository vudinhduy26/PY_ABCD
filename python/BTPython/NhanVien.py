class NhanVien():
    def __init__(self,Ten='',Tuoi=0,Diachi='',TienLuong=0,TongTime=0):
        self.Ten = Ten
        self.Tuoi = Tuoi
        self.Diachi = Diachi
        self.TienLuong = TienLuong
        self.TongTime = TongTime
        self.arr = []
        self.TongTienLuong = 0

    def NhapThongTin(self):
        while True:
            self.Ten = input()
            if self.Ten == "":
                break
            self.Tuoi = int(input())
            self.Diachi = input()
            self.TienLuong = int(input())
            self.TongTime = int(input())
            self.arr.append([self.Ten,str(self.Tuoi),self.Diachi,self.TienLuong,str(self.TongTime)])

    
    def TinhThuong(self):
        for i in range(len(self.arr)):
            if int(self.arr[i][4]) >= 10:
                self.arr[i][3] = str(self.arr[i][3]*(50/100)+self.arr[i][3])
        return self.arr

    def PrintInfo(self):
        return self.arr
    
def main():
    nhanVien = NhanVien()
    nhanVien.NhapThongTin()
    for i in nhanVien.TinhThuong():
        print(" ".join(i))

if __name__ == "__main__":
    main()