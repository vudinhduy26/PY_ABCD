def stray(arr):
    dic = {}
    d = 0
    for i in range(len(arr)):
        if arr[i] in dic:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1
    for j in dic:
        if dic[j] == 1:
            d = j

    return d

print(stray([17, 17, 3, 17, 17, 17, 17]))
