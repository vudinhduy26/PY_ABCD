import re
def solve(s):
    k = 0
    pattern = "[^aeiou]"
    result = re.split(pattern,s)
    for i in result:
        if len(i) > k:
            k = len(i)
    return k
def main():
    print(solve("codewarriors"))

if __name__ == "__main__":
    main()