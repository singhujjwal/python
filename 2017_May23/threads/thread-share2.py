import os
from time import sleep
from threading import Thread

def foo(name, c):
   for i in range(c):
        print "foo [%s]: counting %d" % (name, i)
        sleep(1)


t1 = Thread(target=foo, args=("thread1", 5))
t2 = Thread(target=foo, args=("thread2", 7))

t1.start()
t2.start()

t1.join()
print "Thread 1 exited."

t2.join()
print "Thread 1 exited."
