#!/usr/bin/env python
from threading import Thread, Lock, RLock
import time

data = 0

class TestThread(Thread):
    def __init__(self, tId, lock):
        Thread.__init__(self)
        self.lock = lock
        self.tId = tId
        
    def run(self):
        global data
        while True:
            self.lock.acquire()
            data += 1
            #time.sleep(1)
            print "\n[Thread %d] Data: %d" % (self.tId, data)
            self.lock.release()
            #time.sleep(0)

lock = RLock()
t1 = TestThread(1, lock)
t2 = TestThread(2, lock)

t1.start()
t2.start()
