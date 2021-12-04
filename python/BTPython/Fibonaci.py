def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    arr = [0,1]
    for i in range(1,n+1):
        k = arr[i-1]+arr[i]
        arr.append(k)
        if len(arr) == n:
            break

print(fibonacci(10))