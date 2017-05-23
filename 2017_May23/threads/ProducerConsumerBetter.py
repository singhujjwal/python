from random import randint, random
from time import sleep
from threading import Thread
from Queue import Queue

data = Queue(10)

def producer():
    global data
    while True:
        v = randint(10, 1000)
        print "Produced: ", v, "data: ", data.__dict__['queue']
        data.put(v)
        sleep(random())
        
def consumer():
    global data
    while True:
       v = data.get()
       print "Consumed: ", v, "data:", data.__dict__['queue']
       sleep(random()+1)

p = Thread(target=producer)
c = Thread(target=consumer)

p.start()
c.start()
 


