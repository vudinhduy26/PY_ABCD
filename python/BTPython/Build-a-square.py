def generate_shape(n):
    arr = []
    for i in range(1,n+1):
        if i != n:
            k = n*"+"+"\n"
        else:
            k = n*"+"
        arr.append(k)
    return "".join(arr)

print(generate_shape(3))