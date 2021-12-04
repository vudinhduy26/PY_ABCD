def cooking_time(eggs):
    total_time = 0
    if eggs == 0:
        return 0
    while True:
        total_time += 5
        eggs -= 8
        if eggs <= 0:
            break
    return total_time


print(cooking_time(0))