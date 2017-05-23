#!/usr/bin/env python

import thread
import time
import sys

def print_dot(tid):
    while True:
        print "."
        time.sleep(1)

def print_hash(tid):
    while True:
        print "#"
        time.sleep(1)


thread.start_new_thread(print_dot, (1,))
thread.start_new_thread(print_hash, (2,))

input = raw_input("Enter a string: ")
print "The input was", input


