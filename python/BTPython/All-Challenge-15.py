def rotate(str_):
    k = len(str_)
    d = 1
    arr = []
    while k > 0:
        Lfirst = str_[0:d]
        Lsecond = str_[d:]

        z = Lsecond + Lfirst

        arr.append(z)
        str_ = z
        k -= 1
    return arr


def main():
    print(rotate("123"))

if __name__ == "__main__":
    main()