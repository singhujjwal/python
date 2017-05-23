#!/usr/bin/env python
from threading import Thread
import time

class ThreadOne(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.count = 0
        
    def run(self):
	for i in range(15):
            self.count += 1
            print "Thread one... ", self.count
            time.sleep(1)


class ThreadTwo(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.count = 0
        
    def run(self):
	for i in range(5):
            self.count += 1
            print "Thread two... ", self.count
            time.sleep(1)


t1 = ThreadOne()
t2 = ThreadTwo()

t1.start()
t2.start()

print "Waiting...."
t2.join()
print "Finished t1..."
    
        
