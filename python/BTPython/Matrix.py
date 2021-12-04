def create(str,n):
    string1 = str
    k = 0
    arr = []
    while k < n:
        pT = [string1[i] for i in range(len(string1))]
        arr.append(pT)
        k += 1

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j == i:
                arr[i][j] = string1[0]
    
    for k in range(len(arr)):
        arr[k][len(arr)-1-k] = string1[0]


    return arr

def main():
    maTrix = create('1234',4)
    for i in maTrix:
        print(' '.join(i))

if __name__ == "__main__":
    main()