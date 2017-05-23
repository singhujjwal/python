#!/usr/bin/env python
from threading import Thread
import time

class MyThread(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.count = 0
        
    def run(self):
        while True:
            self.count += 1
            print "Count: ", self.count
            time.sleep(1)

tlist = {} 
for i in xrange(10):
    tlist[i] = MyThread()
    tlist[i].start()

while True:
    print "Main program..."
    time.sleep(1)

    
        
