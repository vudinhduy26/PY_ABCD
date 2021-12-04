import math
def f(n, m):
    z = math.floor(n / m) * m * (m - 1) / 2 + (n % m) * (n % m + 1) / 2
    return int(z)

print(f(15,10))



