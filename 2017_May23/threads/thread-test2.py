import os
from time import sleep
from threading import Thread

def foo():
   for i in range(10):
       print "In foo: counting", i
       sleep(1)


def bar():
   for i in range(10):
       print "In bar: counting", i
       sleep(1)

t1 = Thread(target=foo)
t2 = Thread(target=bar)

t1.start()
t2.start()

t1.join()
print "Thread t1 complete"

t2.join()
print "Thread t2 complete"

for i in range(10):
    print "In main: counting", i
    sleep(1)


        


