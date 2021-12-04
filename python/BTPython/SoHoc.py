class SoHoc():
    def __init__(self,number1=0,number2=0):
        self.__number1 = number1
        self.__number2 = number2
    def inputinfo(self):
        self.__number1,self.__number2 = map(int,input().split())
        return self.__number1,self.__number2
    def printinfo(self):
        print(self.__number1,self.__number2)
    def addition(self):
        return self.__number1 + self.__number2

def main():
    sohoc = SoHoc()
    sohoc.inputinfo()
    print("TOng 2 SO : ",sohoc.addition())

if __name__ == "__main__":
    main()