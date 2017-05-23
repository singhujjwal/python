from time import sleep
from random import random, randint

def producer(pipe):
    while True:
        val = randint(10, 1000)
        print "producer: produced data %d\n" % val
        pipe.send(val)
        sleep(random())


def consumer(pipe):
    while True:
        val = pipe.recv() 
        print "consumer: received %d\n" % val
        sleep(random())


