from __future__ import print_function
from time import sleep

#from threading import Thread

from multiprocessing import Process as Thread

def foo():
    for i in range(10):
        print("In foo counting", i)

def bar():
    for i in range(10):
        print("In bar counting", i)

t1 = Thread(target=foo)
t2 = Thread(target=bar)

t1.start()
t2.start()

