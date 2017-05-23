from threading import Thread, current_thread
import time

def foo():
    i = 0
    while True:
        if current_thread().interrupted: break
        print "Foo: counting", i
        i += 1

t1 = Thread(target=foo)

t1.interrupted = False
t1.start()

time.sleep(5)
t1.interrupted = True
