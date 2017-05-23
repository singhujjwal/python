#!/usr/bin/env python

import thread
import time

def child(tid):
    count = 0
    while True:
        print "Thread:", tid, "Count:", count
        count += 1
   #     time.sleep(1)

def parent():
    for I in range(10): 
        thread.start_new_thread(child, (I,))

parent()
count = 0
while 1:
    time.sleep(1)
    print "---------- Main program: ", count
    count += 1

