from threading import Thread, Lock
from random import random
from time import sleep

SIZE = 1000000
a = range(SIZE)

update_a = Lock()

def foo():
    for i in range(len(a)):
        with update_a:
            a[i] = a[i] * a[i]

def bar():
    for i in range(len(a)):
        with update_a:
           #update_a.acquire()
            a[i] = a[i] * a[i]
           #update_a.release()


t1 = Thread(target=foo)
t2 = Thread(target=bar)

t1.start()
t2.start()

t1.join()
t2.join()

for i, j in zip(a, range(SIZE)):
    if i != (j ** 4): print(i)



