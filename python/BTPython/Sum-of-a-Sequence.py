import math
def sequence_sum(begin_number, end_number, step):
    b = begin_number
    e = end_number
    s = step

    n = math.floor((e - b) / s) + 1
    if n <= 0:  return 0
    return (2*b + s*(n-1)) * n // 2

print(sequence_sum(20, 673388797, 5))
