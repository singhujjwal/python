from threading import Thread
from itertools import count
from time import sleep

stop_foo = False

def foo():
    for i in count(1):
        print "In foo: counting", i
    #    sleep(1)
        if stop_foo: break


def bar():
    for i in count(1):
        print "In bar: counting", i
     #   sleep(1)
   


t1 = Thread(target=foo)
t2 = Thread(target=bar)

t1.start()
t2.start()

