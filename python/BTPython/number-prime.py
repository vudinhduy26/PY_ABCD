import math
def is_prime(num):
    if num <= 0 or num == 1:
        return False
    else:
        k = True
        for i in range(2,round(math.sqrt(num))+1):
            if num % i == 0:
                k = False
                break
            else:
                k = True
        return k

print(is_prime(7))