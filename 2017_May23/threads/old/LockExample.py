#!/usr/bin/env python

import thread
import time

def child(tid, lock):
    while 1:
        lock.acquire()
        print "Hi, from thread:", tid
        time.sleep(1)
        lock.release()
        time.sleep(1)  # why? 

def parent():
    lock = thread.allocate_lock()
    for i in range(10): 
        thread.start_new_thread(child, (i,lock))

if __name__ == "__main__":
    parent()
    while 1: pass