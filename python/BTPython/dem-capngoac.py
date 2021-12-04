def count(string):
    dictt = {}
    k = 0
    for i in string:
        if i not in dictt:
            dictt[i] = 1
        else:
            dictt[i] += 1
    if dictt['('] > dictt[")"]:
        k = dictt[")"]
        return k
    else:
        k = dictt["("]
        return k


def main():
    print(count("(((((((((()"))

if __name__ == "__main__":
    main()