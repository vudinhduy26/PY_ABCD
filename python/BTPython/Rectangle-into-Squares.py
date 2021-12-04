def sqInRect(x, y):
    if x == y:
        return None
    arr = []
    while x != y:
        if x > y:
            x -= y
            arr.append(y)
        elif x < y:
            y -= x
            arr.append(x)
    arr.append(y)
    return arr

print(sqInRect(20,14))