def number(lines):
    arr = []
    for i in range(len(lines)):
        k = i+1
        arr.append(str(k)+": "+lines[i])
    return arr

def main():
    print(number(["a", "b", "c"]))

if __name__ == "__main__":
    main()