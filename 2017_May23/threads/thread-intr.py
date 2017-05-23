import os
from time import sleep
from threading import Thread, current_thread
from itertools import count

def foo():
   for i in count(0):
        if hasattr(current_thread(), "stop"): break
        print "In foo: counting", i

t1 = Thread(target=foo)
t1.start()

sleep(5)
t1.stop = True



