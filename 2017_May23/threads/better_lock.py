from threading import RLock

def foo():
    with Rlock() as lock:
        print "In critical region..."
        for i in range(10): print i,
        print "Exiting critical region..."


