

def largest_cross_sum(arr): 
    h, w = range(len(arr)), range(len(arr[0]))
    rows = [sum(row) for row in arr]
    brr = []
    cols = []
    t = []
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            brr.append(arr[j][i])
        cols.append(sum(brr))
        brr = []
    for k in h:
        for g in w:
          t.append(rows[k] + cols[g] - arr[k][g])
    #return max(rows[j] + cols[i] - arr[j][i] for j in h for i in w)
    return max(t)

def main():
    k = [[1, 1, 1, 4, 1, 1, 1],
                   [3, 3, 3, 3, 3, 3, 3],
                   [1, 1, 1, 4, 1, 1, 1]]
    print(largest_cross_sum(k))

if __name__ == "__main__":
    main()