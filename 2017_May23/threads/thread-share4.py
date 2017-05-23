from threading import Thread
from threading import RLock
from time import sleep

i = 0
l = RLock()

def foo(name):
    global i
    global l
    while True: 
        l.acquire()
        print "Thread [%s]: Counting %d" % (name, i)
        i += 1
        l.release()

t1 = Thread(target=foo, args=("thread1",))
t2 = Thread(target=foo, args=("thread2",))

t1.start()
t2.start()


