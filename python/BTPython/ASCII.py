def uni_total(s):
    total = 0
    for i in s:
        total += ord(i) 
    return total

def main():
    print(uni_total("Mary had a little lamb"))

if __name__ == "__main__":
    main()