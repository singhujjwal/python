from random import randint, random
from time import sleep
from threading import Thread, Condition

class MyQueue:
    def __init__(self, size=10):
        self.maxsize = 10
        self.data = []
        self.full = Condition()
        self.empty = Condition()

    def put(self, v):
        self.full.acquire()
        if len(self.data) > self.maxsize:
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

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)

data = MyQueue(10)

def producer():
    while True:
        v = randint(10, 1000)
        print "Produced: ", v, "data: ", data
        data.put(v)
        sleep(random())
        
def consumer():
    while True:
       v = data.get()
       print "Consumed: ", v, "data:", data
       sleep(random()+1)

p = Thread(target=producer)
c = Thread(target=consumer)

p.start()
c.start()
 


