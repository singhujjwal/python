from threading import Thread, Condition, RLock
from time import sleep
from random import randint
from collections import deque

class SimpleQueue:
    def __init__(self, size=10):
        self.empty_slots = size
        self.queue = deque()
        self.empty = Condition()
        self.full = Condition()
        self.lock = Lock()

    def show(self):
        with self.lock: r = str(self.queue)
        return r

    def put(self, v):
        with self.full:
            if not self.empty_slots: self.full.wait()

        with self.empty:
            with self.lock:
                self.queue.append(v)
            self.empty_slots -= 1
            self.empty.notify()

    def get(self):
        with self.empty:
            if len(self.queue) == 0: self.empty.wait()

        with self.full:
            with self.lock:
                v = self.queue.popleft()
            self.empty_slots += 1
            self.full.notify()

        return v


queue = SimpleQueue(10)

def producer():
    while True:
        v = randint(1, 100)
        print "Produced: ", v, "Queue =", queue.show()
        queue.put(v)
        sleep(v/50.0)


def consumer():
    while True:
        v = queue.get()
        print "Consumed: ", v, "Queue =", queue.show() 
        sleep(v/150.0)

p = Thread(target=producer)
c = Thread(target=consumer)

p.start()
c.start()

