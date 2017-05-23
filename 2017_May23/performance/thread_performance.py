#from threading import Thread
from multiprocessing import Process as Thread

from performance import timeit, print_log

def worker(w):
    y = 0
    print "Starting worker:", w
    for i in range(1000000):
        for j in range(10000):
            y += i*j
    print "Worker", w, "complete..."

@timeit
def start_workers():
    pool = { }
    for i in range(16):
        pool[i] = Thread(target=worker, args=(i,))
        pool[i].start()
    print "Created 16 workers..."

    for i in range(16):
        pool[i].join()
    print "All workers complete..."

start_workers()

print_log()

