def partitions_dp(n):
    partitions_of = []
    partitions_of.append([()])
    partitions_of.append([(1,)])
    for num in range(2, n+1):
        ptitions = set()
        for i in range(num):
            for partition in partitions_of[i]:
                ptitions.add(tuple(sorted((num - i, ) + partition)))
        partitions_of.append(list(ptitions))
    return len(partitions_of[n])


print(partitions_dp(5))