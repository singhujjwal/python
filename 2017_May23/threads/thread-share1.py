import os
from time import sleep
from threading import Thread
from itertools import count

def foo(name, th):
   for i in count(0):
        if hasattr(th, "stop"): break
        print "foo [%s]: counting %d" % (name, i)

class MyThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.thname = name

    def run1(self):
        foo(self.thname, self)


t1 = MyThread("thread1")
t2 = MyThread("thread2")

t1.start()
t2.start()

sleep(5)
t1.stop = True

sleep(3)
t2.stop = True

