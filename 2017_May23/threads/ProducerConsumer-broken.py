from random import randint, random
from time import sleep
from threading import Thread

data = []

def producer():
    global data
    while True:
        v = randint(10, 1000)
        print "Produced: ", v
        data.append(v)
        sleep(random())

def consumer():
    global data
    while True:
       v = data.pop(0)
       print "Consumed: ", v
       sleep(random())


p = Thread(target=producer)
c = Thread(target=consumer)

p.start()
c.start()
 


