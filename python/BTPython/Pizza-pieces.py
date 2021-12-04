def max_pizza(cuts):
    k = 0
    z = 1
    for i in range(0,cuts+1):
        k = i + z
        z = k
    return k


print(max_pizza(6))