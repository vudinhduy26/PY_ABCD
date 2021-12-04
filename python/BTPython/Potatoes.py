def potatoes(p0, w0, p1):
    x = ((p0*0.01)*w0 - (p1*0.01)*w0)/(1-(p1*0.01))
    return int(w0 - x)

print(potatoes(93, 129, 91))