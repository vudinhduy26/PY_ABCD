def duplicate_count(text):
    dicta = {}
    arr = []
    for i in text.lower():
        if i in dicta:
            dicta[i] += 1
        else:
            dicta[i] = 1
    for j in dicta:
        if dicta[j] >= 2:
            arr.append(j)
    return len(arr)
print(duplicate_count("Indivisibilities"))