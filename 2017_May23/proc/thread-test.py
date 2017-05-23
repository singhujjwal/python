import os
from time import sleep
#from threading import Thread
from multiprocessing import Process as Thread

def foo():
   for i in range(10):
       print "In foo: counting", i
       sleep(0.5)

t1 = Thread(target=foo)
t1.start()

print "Back to main program..."
for i in range(5):
    print "Main: counting:", i
    sleep(0.5)

t1.join()





