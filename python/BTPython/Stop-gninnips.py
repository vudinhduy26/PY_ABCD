def reversed(n):
    a = n[::-1]
    return a

def spin_words(sentence):
    arr = []
    for i in sentence.split(" "):
        if len(i) >= 5:
            arr.append(reversed(i))
        else:
            arr.append(i)
    
    return " ".join(arr)


def main():
    print(spin_words("This is another test"))

if __name__ == "__main__":
    main()