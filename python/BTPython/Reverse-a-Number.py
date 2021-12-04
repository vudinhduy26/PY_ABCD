def reverse_number(n):
    a = str(n)
    
    if a[0] == "-":
        b = a[0]
        strr = a[1:]
        return int(b+strr[::-1])
    else:
        strr = a[::-1]
        return int(strr)
    

print(reverse_number(10000))