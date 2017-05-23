from threading import Thread, RLock
from time import sleep
from random import random

count = 0

lock = RLock()

def foo():
    global count

    for i in range(10):
        count += 1
        lock.acquire()
        print "In foo: count set to", count
        sleep(random())
        print "In foo: count now is", count
        lock.release()
        sleep(.1)

def bar():
    global count

    for i in range(10):
        count += 1
        lock.acquire()
        print "In bar: count =", count
        sleep(random())
        print "In bar: count =", count
        lock.release()
        sleep(.1)

t1 = Thread(target=foo)
t2 = Thread(target=bar)
t1.start()
t2.start()

