from threading import Thread, Lock
from time import sleep
from random import random


def foo(data_lock):
    for i in range(10):
        with data_lock:
            print "foo: counting", i
            sleep(1)
        sleep(0.1)

def bar(data_lock):
    for i in range(10):
        with data_lock:
            print "bar: counting", i
            sleep(1)
        sleep(0.1)

data_lock = Lock()

t1 = Thread(target=foo, args=(data_lock,))
t2 = Thread(target=bar, args=(data_lock,))

t1.start()
t2.start()


