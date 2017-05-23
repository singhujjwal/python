import os
from time import sleep
from threading import Thread
from itertools import count

def foo(name):
   for i in count(0):
        if hasattr(t1, "stop"): break
        print "foo [%s]: counting %d" % (name, i)


t1 = Thread(target=foo, args=("thread1",))
t2 = Thread(target=foo, args=("thread2",))

t1.start()
t2.start()

sleep(5)
t1.stop = True

