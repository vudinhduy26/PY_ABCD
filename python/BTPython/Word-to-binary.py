def word_to_bin(word):
    arr = []
    for i in word:
        k = "0"+"{0:b}".format(ord(i))
        arr.append(k)
    return arr

print(word_to_bin('Yosemite'))