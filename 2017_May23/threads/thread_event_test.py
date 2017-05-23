from threading import Thread, Event
from random import random
from time import sleep

a = range(20) 
updated = Event()
read = Event()

def foo():
    for i in range(len(a)):
        read.wait()
        read.clear()
        a[i] = a[i] * a[i] 
        print "foo: updated", i, "=", a[i]
        updated.set()
        sleep(random())

def bar():
    for i in range(len(a)):
        read.set()
        updated.wait()
        updated.clear()
        print "In bar:", i, "=", a[i]
        sleep(random())


t1 = Thread(target=foo)
t2 = Thread(target=bar)

t1.start()
t2.start()

t1.join()
t2.join()
print "a =", a



