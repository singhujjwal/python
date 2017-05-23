import time
from threading import Thread

def foo():
    for i in range(10):
        print "In foo: counting ", i
        time.sleep(1)

def bar():
    for i in range(10):
        print "In bar: counting ", i
        time.sleep(1)


t1 = Thread(target=foo)
t2 = Thread(target=bar)

t1.start()
t2.start()

for i in range(10):
    print "In main: counting", i
    time.sleep(1)

