
a = [11, 22, 33, 44, 55, 66, 77]


def cycle(l):
    length = len(l)
    i = 0

    while True:
        yield l[i]
        i += 1
        if i >= length: i = 0

from itertools import cycle

for n in cycle(a):
    print n
