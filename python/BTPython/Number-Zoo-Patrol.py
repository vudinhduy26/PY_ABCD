def find_missing_number(numbers):
    k = len(numbers)
    return int(((k+2)*(k+1))/2 - sum(numbers))

print(find_missing_number([2, 3, 4]))