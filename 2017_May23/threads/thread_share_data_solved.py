from threading import Thread, Lock
from random import random
from time import sleep

SIZE = 10000

a = range(SIZE)

def update(i):
    a[i] = a[i] * a[i]

def foo():
    for i in xrange(SIZE):
        update(i)

def bar():
    for i in xrange(SIZE):
        update(i)


t1 = Thread(target=foo)
t2 = Thread(target=bar)

b = list(a)

t1.start()
t2.start()

t1.join()
t2.join()

for i, v in enumerate(a):
    if (b[i] ** 4) != v:
        print "a[{}] = {} NOT consistent with b[{}] ** 4 = {}".format(
                                                    i, v, i, b[i] ** 4)


