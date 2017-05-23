#!/usr/bin/env python
import time
import random
import thread


def child(tid):
	while True:
		print "Thread ", tid, "running: ", random.randint(1, 100000)
#		time.sleep(1)


for i in range(10):
	print "Starting thread: ", i
	thread.start_new_thread(child, (i,))


while True: 
    print "Main thread running..."



