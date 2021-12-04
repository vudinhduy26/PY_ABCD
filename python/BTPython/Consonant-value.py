import re

def handle(n):
    k = 0
    for i in n:
        k += ord(i)-96
    return k

def solve(s):
    arr = [] 
    pattern = "[aeiou]"
    result = re.split(pattern,s)
    for i in result:
        if len(i) > 1:
            arr.append(handle(i))
        elif i == "":
            continue
        else:
            arr.append(ord(i)-96)
    return max(arr)

def main():
    print(solve("twelfthstreet"))

if __name__ == "__main__":
    main()