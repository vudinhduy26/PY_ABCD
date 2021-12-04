import math

def scp(k):
    arr1 = []
    for i in range(0,k//2+1):
        if round(math.sqrt(i))**2 == i:
            arr1.append(i)
    return arr1
def all_squared_pairs(n):

    arr = []
    for i in scp(n):
        a = n - i
        if round(math.sqrt(a))**2 == a:
            arr.append([round(math.sqrt(i)),round(math.sqrt(a))])

    return arr

print(all_squared_pairs(147))