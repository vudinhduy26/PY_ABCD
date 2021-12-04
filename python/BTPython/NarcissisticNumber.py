def narcissistic( value ):
    string1 = str(value)
    iDnumber = len(str(value))
    check = 0
    for i in string1:
        check += int(i)**iDnumber
    if check == value:
        return True
    return False

print(narcissistic(153))