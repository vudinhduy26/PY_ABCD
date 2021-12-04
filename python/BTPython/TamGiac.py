def create(n):
    arr = [int(i) for i in n.split() ]
    brr = []
    crr = [arr]
    while True:
        for i in range(len(arr)-1):
            brr.append(arr[i]+arr[i+1])
        crr.append(brr)
        f = brr
        arr = f
        brr = []
        if len(arr) == 1:
            break
    return crr[::-1]

def main():
    n = input()
    for i in create(n):
        print(i)

if __name__ == "__main__":
    main()



