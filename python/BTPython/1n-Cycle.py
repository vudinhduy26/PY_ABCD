def cycle(n) :
    if n%2==0 or n%5==0:
        return -1
    else:
        res = 10%n
        c = 1
        while res != 1:
            res = res*10 % n
            c+=1
    return c


print(cycle(98))
