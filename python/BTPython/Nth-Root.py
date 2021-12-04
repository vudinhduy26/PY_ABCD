
def nth_root_equals_digit_sum(n):
    arr = []
    for i in range(1,1000):
        k = sum([int(i) for i in str(i**n)])
        if k == i:
            arr.append(i**n)
    return arr
def main():
    print(nth_root_equals_digit_sum(2))

if __name__ == "__main__":
    main()