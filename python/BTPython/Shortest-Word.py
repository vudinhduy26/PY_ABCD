def find_short(s):
    k = 10
    arr = s.split(" ")
    for i in arr:
        if len(i) < k:
            k = len(i) 
    return k # l: shortest word length

def main():
    print(find_short("bitcoin take over the world maybe who knows perhaps"))

if __name__ == "__main__":
    main()