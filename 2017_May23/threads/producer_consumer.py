from threading import Thread
from time import sleep
from random import randint, random
from collections import deque

queue = deque()

def producer():
    while True:
        v = randint(1, 100)
        print "Produced: ", v
        queue.append(v)
        sleep(v/100.0)


def consumer():
    while True:
        sleep(random())
        v = queue.popleft()
        print "Consumed: ", v

p = Thread(target=producer)
c = Thread(target=consumer)

p.start()
c.start()

