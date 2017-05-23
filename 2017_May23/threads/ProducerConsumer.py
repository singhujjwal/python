from random import randint, random
from time import sleep
from threading import Thread, Condition


data = []
maxsize = 10

full  = Condition()
empty = Condition()


def producer():
    global data
    global full
    global empty 
    global maxsize

    while True:
        full.acquire()
        if len(data) > maxsize:
           full.wait()
        full.release()
        
        v = randint(10, 1000)
        print "Produced: ", v, "data: ", data
        data.append(v)
        empty.acquire()
        empty.notify()
        empty.release()
        sleep(random())
        
def consumer():
    global data
    global full
    global empty

    while True:
       empty.acquire()
       if len(data) < 1:
          empty.wait()
       empty.release()

       v = data.pop(0)
       print "Consumed: ", v, "data:", data
       full.acquire()
       full.notify()
       full.release()
       sleep(random()+1)

p = Thread(target=producer)
c = Thread(target=consumer)

p.start()
c.start()
 


