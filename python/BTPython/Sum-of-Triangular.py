def sum_triangular_numbers(n):
    sum_ = 0
    arr = []
    for i in range(1,n+1):
        sum_ += i
        arr.append(sum_)
    return sum(arr)

print(sum_triangular_numbers(6))