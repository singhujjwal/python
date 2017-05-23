#!/usr/bin/env python

import thread
import time

def child(tid):
    print "Hi, from thread:", tid
    time.sleep(1)

def parent():
    for I in range(10): 
        thread.start_new_thread(child, (I,))

if __name__ == "__main__":
    parent()
    while 1:
        time.sleep(1)
        print "."

