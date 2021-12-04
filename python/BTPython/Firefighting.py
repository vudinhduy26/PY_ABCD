from typing import Counter

def createarr(strr,w):
    arr = []
    k = w
    a = 0
    z = len(strr)
    while z > 0:
        arr.append(strr[a:w])
        a += k
        w += k
        z-=k
    return arr

def waterbombs(fire, w):
    strr = fire.split("Y")
    qrr = []
    hrr = []
    rrr = []
    for i in strr:
        if i == "":
            continue
        else:
            qrr.append(i)
    for j in qrr:
        hrr.append(createarr(j,w))
    for z in hrr:
        for l in z:
            rrr.append(l)
    return len(rrr)


print(waterbombs("YYYxxxxxxxYxxYxxxxxY",2))