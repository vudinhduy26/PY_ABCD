import re
def test(n):
    rex = re.compile(r'^ *a* *b* *c* *d* *e* *f* *g* *h* *i* *j* *k* *l* *m* *n* *o* *p* *q* *r* *s* *t* *u* *v* *w* *x* *y* *z* *\Z')
    return rex.match(n)

print(test("asdfg"))