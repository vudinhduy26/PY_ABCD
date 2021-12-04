def get_score(n):
    k = 0
    m = 0
    z = 0
    for i in range(1,n+1):
        k += 50 + z
        z += 50
    return k

print(get_score(2))