import math


def get_sum_of_propers(n):
    sum = 0
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            sum += x
            if x != n // x:
                sum += n // x
    return sum

def buddy(start, limit):
    for n in range(start, limit+1):
        m = get_sum_of_propers(n) 
        if n < m and n == get_sum_of_propers(m) :
            return [n, m]
    return "Nothing"

print(buddy(10,50))