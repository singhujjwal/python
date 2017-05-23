from random import random
from time import sleep
from multiprocessing import Process as Thread, Lock


a = range(20) 
lock = Lock()

def foo():
    for i in range(len(a)):
        lock.acquire()
        a[i] = a[i] * a[i] 
        print "foo: updated", i
        lock.release()
        sleep(0.01)

def bar():
    for i in range(len(a)):
        lock.acquire()
        a[i] = a[i] * a[i] 
        print "bar: updated", i
        lock.release()
        sleep(0.01)


t1 = Thread(target=foo)
t2 = Thread(target=bar)

t1.start()
t2.start()

t1.join()
t2.join()
print "a =", a



