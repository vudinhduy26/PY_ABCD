def nenxau(xau):
    d = {}
    c = []
    for i in n:
        if i in d:
            d[i] +=1
        else:
            d[i] = 1
    for j in d:
        c.append(str(d[j])+j)
    return ''.join(c)

def giainenxau(xaux):
    c = []
    h = []
    for i in l:
        c.append(i)
    for j in range(len(c),2):
        if j%2!=0:
            h.append(c[j]*int(c[j-1]))
    return ''.join(h)

n = input()
l = input()
print(nenxau(n))
print(giainenxau(l))
"""def giaithua(n):
    if n == 1:
        return 1
    return giaithua(n-1)*n

a = int(input())
dem = 0
nn = []
while dem<a:
    m = int(input())
    dem +=1
    nn.append(m)
for i in nn:
    print(giaithua(i))"""