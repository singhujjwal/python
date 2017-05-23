from threading import Thread, RLock as Lock
from random import random
from time import sleep

SIZE = 10000

a = range(SIZE)
a_lock = Lock()


def nullify_three_multiples(i):
    with a_lock:
        if a[i] % 3 == 0: a[i] = 0

def square_list_item(i):
    with a_lock:
        a[i] = a[i] * a[i]
        nullify_three_multiples(i)

    #square_lock.acquire()
    #a[i] = a[i] * a[i]
    #square_lock.release()

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


