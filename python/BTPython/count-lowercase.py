import re
def lowercase_count(strng):
    patter = re.compile(r'[a-z]')
    result = patter.findall(strng)
    return len(result)


def main():
    print(lowercase_count('ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~'))

if __name__ == "__main__":
    main()