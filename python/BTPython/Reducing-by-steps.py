import math

def maxi(x,y):
    if x > y:
        return x
    else:
        return y

def mini(x,y):
    if x < y:
        return x
    else:
        return y

def som(x,y):
    return x+y

def gcdi(x,y):
    k = int(math.gcd(abs(x),abs(y)))
    return k

def lcmu(x,y):
    return int((abs(x)*abs(y))/gcdi(x,y))

def oper_array(fct, arr, init):
    brr = []
    for i in range(len(arr)):
        k = fct(arr[i],init)
        brr.append(k)
        init = k
    return brr

a = [18, 69, -90, -78, 65, 40]
print(oper_array(lcmu,a,a[0]))