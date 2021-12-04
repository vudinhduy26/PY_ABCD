def row_weights(array):
    n = 2
    k = 0
    z = 0
    brr = []
    for i in range(len(array)):
        if (i+n)%2==0:
            k += array[i]
            brr.append(k)
        else:
            z += array[i]
            brr.append(z)
    return k,z


print(row_weights([50,60,70,80]))