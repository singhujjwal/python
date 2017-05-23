from random import randint, random
from time import sleep
from threading import Thread, Condition

class Queue:
    
    def __init__(self, size):
        self.data = []
        self.size = size
        self.full  = Condition()
        self.empty = Condition()

    def put(self, v):
        self.full.acquire()
        if len(self.data) > self.size:
           self.full.wait()
        self.full.release()

        self.data.append(v)

        self.empty.acquire()
        self.empty.notify()
        self.empty.release()

    def get(self):
       self.empty.acquire()
       if len(self.data) < 1:
          self.empty.wait()
       self.empty.release()

       v = self.data.pop(0)
       self.full.acquire()
       self.full.notify()
       self.full.release()

       return v

queue = Queue(10)


def producer():
    while True:
        v = randint(10, 1000)
        print "Produced: ", v
        queue.put(v)
        sleep(random())
        
def consumer():
    while True:
       v = queue.get()
       print "Consumed: ", v
       sleep(random()+1)

p = Thread(target=producer)
c = Thread(target=consumer)

p.start()
c.start()
 


