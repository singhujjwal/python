#!/usr/bin/env python

import thread
import time

def child(tid):
    while True:
        print "."
        time.sleep(1)



thread.start_new_thread(child, (1,))
while True:
	input = raw_input("Enter a string: ")
	print "The input was", input


