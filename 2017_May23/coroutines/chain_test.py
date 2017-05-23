a = [10, 20, 30, 40]
b = [40, 50, 60, 70]
c = [80, 90, 100, 120]

#for i in a + b + c:
#    print i

def chain(*args):
    for c in args:
        for i in c:
            yield i

from itertools import chain

for i in chain(a, b, c):
    print i
