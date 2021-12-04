class Tinh():
    def __init__(self,arr=[]):
        self.arr = arr
        self.k = 0
        self.f = 0
    
    def People(self):
        for i in range(len(self.arr)):
            self.k += self.arr[i][0]
            self.f += self.arr[i][1]
        return self.k - self.f


def main():
    people = Tinh([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])
    print(people.People())

if __name__ == "__main__":
    main()