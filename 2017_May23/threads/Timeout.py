#!/usr/bin/env python

import thread
import time
import sys

def timeout(t):
	while True:
		print "."
		time.sleep(1)



thread.start_new_thread(timeout, (1,))
input = raw_input("Enter a string: ")
print "The input was", input


