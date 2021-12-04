def validate_word(word):
    dictt = {}
    for i in word.lower():
        if i in dictt:
            dictt[i] += 1
        else:
            dictt[i] = 1
    k = dictt[i]
    c = True
    for j in dictt:
        if dictt[j] == k:
            c = True
        else:
            c = False
            break
    return c

print(validate_word("?!?!?!"))