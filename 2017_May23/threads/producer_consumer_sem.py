from threading import Thread, Semaphore, RLock
from time import sleep
from random import randint
from collections import deque

class SimpleQueue:
    def __init__(self, size):
        self.queue = deque()
        self.reader = Semaphore(0)
        self.writer = Semaphore(size)
        self.lock = RLock()


    def put(self, v):

        self.writer.acquire()

        with self.lock: self.queue.append(v)

        self.reader.release()

    def get(self):
        self.reader.acquire()

        with self.lock: v = self.queue.popleft()

        self.writer.release()

        return v


queue = SimpleQueue(10)

def producer():
    while True:
        v = randint(1, 100)
        print "Produced: ", v
        queue.put(v)
        #sleep(v/100.0)


def consumer():
    while True:
        v = queue.get()
        print "Consumed: ", v
        sleep((v/100.0) + 0.3)

p = Thread(target=producer)
c = Thread(target=consumer)

p.start()
c.start()

