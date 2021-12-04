def duplicate_encode(word):
    dictt = {}
    arr = []
    for i in word.lower():
        if i in dictt:
            dictt[i] += 1
        else:
            dictt[i] = 1
    for j in word.lower():
        if dictt[j] > 1:
            arr.append(")")
        else:
            arr.append("(")
    return "".join(arr)

print(duplicate_encode("Success"))