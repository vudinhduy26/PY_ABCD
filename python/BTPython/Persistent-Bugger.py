def persistence(n):
    str_ = str(n)
    k = 1
    count = 0
    while True:
        for i in str_:
            k *= int(i)
        if len(str_) == 1:
            break
        else:
            count += 1
            f = str(k)
            str_ = f
            k = 1
    return count

print(persistence(25))