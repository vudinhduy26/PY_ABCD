import re

def solve(s):
    k = s
    pattern1 = "[a-z]"
    result1 = re.findall(pattern1,s)
    pattern2 = "[A-Z]"
    result2 = re.findall(pattern2,s)
    if len(result1) == len(result2):
        return k.lower()
    elif len(result1) > len(result2):
        return k.lower()
    elif len(result1) < len(result2):
        return k.upper()

def main():
    print(solve("CODe"))

if __name__ == "__main__":
    main()