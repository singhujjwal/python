import os
from time import sleep
from threading import Thread
from itertools import count

def foo():
   for i in count(0):
        if hasattr(t1, "interrupt") and getattr(t1, "interrupt"): 
           break
        print "In foo: counting", i

t1 = Thread(target=foo)
t1.start()

sleep(5)
t1.interrupt = True




