#from threading import Thread
from multiprocessing import Process as Thread
from time import sleep

def foo(t):
    for i in range(10):
        print t, "counting", i
        sleep(1)

threads = {}
for i in range(10):
    threads[i] = Thread(target=foo, args=(i,))
    threads[i].start()


print "Waiting for threads to complete..."
for t in threads.values(): t.join()

