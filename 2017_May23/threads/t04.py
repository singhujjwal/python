from time import sleep
from threading import Thread
from threading import RLock

class MyData:
    
    def __init__(self):
        self.data = [10, 20, 30]
        self.lock = RLock()

    def get_values(self):
        self.lock.acquire()
        values = tuple(self.data)
        self.lock.release()
        return values

    def set_values(self, *values):
        self.lock.acquire()
        for i, v in enumerate(self.data):
            self.data[i] = values[i]
        self.lock.release()



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

