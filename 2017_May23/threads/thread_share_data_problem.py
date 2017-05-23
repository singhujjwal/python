from threading import Thread
from random import random
from time import sleep

SIZE = 10000

a = range(SIZE)

def square_list_item(i):
    a[i] = a[i] * a[i]

def square_list():
    for i in xrange(SIZE):
        square_list_item(i)


t1 = Thread(target=square_list)
t2 = Thread(target=square_list)

b = list(a)

t1.start()
t2.start()

t1.join()
t2.join()

for i, v in enumerate(a):
    if (b[i] ** 4) != v:
        print "a[{}] = {} NOT consistent with b[{}] ** 4 = {}".format(
                                                    i, v, i, b[i] ** 4)


