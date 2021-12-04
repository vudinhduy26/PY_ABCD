def count_squares(n):
    a = 0
    for i in range(1,n+1):
        a += i*i
    return a

print(count_squares(3))