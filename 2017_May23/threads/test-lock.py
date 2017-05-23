from threading import Thread, Lock
from random import random, randint
from time import sleep

data = 0
lock = Lock()

def synchronized(f):
    def wrapper(name):
        global lock
        lock.acquire()
        r = f(name)
        lock.release()
        sleep(0.01)
        return r
    return wrapper

@synchronized
def show_data(name):
    global data
    data = randint(10, 100)
    print "In", name, ": Generated value:", data
    sleep(random())
    print "In", name, ": The value now is: ", data
 
def test_function(name):
    global data
    while True:
        show_data(name)

t1 = Thread(target=test_function, args=("thread-1",))
t2 = Thread(target=test_function, args=("thread-2",))


t1.start()
t2.start()


