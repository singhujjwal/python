from time import sleep
from threading import Thread
from threading import RLock

i = 0

lock = RLock()

def foo(name):
    global i
    while i < 10:
        lock.acquire()
        print "In", name, ": counting", i
        sleep(0.5)
        print "In", name, "i = ", i
        i += 1
        lock.release()




t1 = Thread(target=foo, args=("thread1",))
t2 = Thread(target=foo, args=("thread2",))

t1.start()
t2.start()

foo("main")

t1.join()
t2.join()

