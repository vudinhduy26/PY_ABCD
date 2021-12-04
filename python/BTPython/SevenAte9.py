import re
def seven_ate9(str_):
    arr = []
    for i in range(len(str_)-1):
        if str_[i] == '9' and str_[i+1] == '7' and str_[i-1] == '7':
            arr.append("")
        else:
            arr.append(str_[i])
    arr.append(str_[len(str_)-1])
    return "".join(arr)
print(seven_ate9('79797'))