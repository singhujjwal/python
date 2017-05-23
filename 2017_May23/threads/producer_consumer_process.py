from multiprocessing import Process, Queue 
from time import sleep
from random import randint
from collections import deque

queue = Queue(10)

def producer():
    while True:
        v = randint(1, 100)
        print "Produced: ", v, "Queue =", queue
        queue.put(v)
        sleep(v/100.0)


def consumer():
    while True:
        v = queue.get()
        print "Consumed: ", v, "Queue =", queue
        sleep((v/100.0) + 0.3)

p = Process(target=producer)
c = Process(target=consumer)

p.start()
c.start()

