import re
def remove_chars(s):
    pattern = r"[a-zA-Z\s]"
    result = re.findall(pattern,s)
    return ''.join(result)

print(remove_chars('my_list = ["a","b","c"]'))
