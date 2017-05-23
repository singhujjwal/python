from threading import Thread
from itertools import count
from time import sleep

stop_foo = False

def foo():
    for i in count(1):
        print "In foo: counting", i
    #    sleep(1)
        if stop_foo: break


t1 = Thread(target=foo)
t1.start()

for i in range(5):
    print "In main: counting", i
    sleep(1)

stop_foo = True


