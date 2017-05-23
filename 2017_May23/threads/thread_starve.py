from threading import Thread, Lock
from random import random
from time import sleep

lock = Lock()
SIZE = 50

def foo():
    for i in range(SIZE):
        with lock:
            print "Foo thread: counting:", i
            sleep(0.2)

def bar():
    for i in range(SIZE):
        with lock:
            print "Bar thread: counting:", i
            sleep(0.2)


t1 = Thread(target=foo)
t2 = Thread(target=bar)

t1.start()
t2.start()

t1.join()
t2.join()



