def createMatrix(m,n):
    arr = []
    while m > 0:
        k = input().split()
        pT = [int(i) for i in k[:n]]
        arr.append(pT)
        m -= 1
    return arr


def main():
    m,n = map(int,input().split())
    maTrix = createMatrix(m,n)
    for row in maTrix:
        print(row)

if __name__ == "__main__":
    main()