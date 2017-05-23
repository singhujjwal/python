from time import sleep
from threading import Thread

def foo():
    for i in range(10):
        sleep(1)
        print "In foo: counting", i


def bar():
    for i in range(30):
        sleep(1)
        print "In bar: counting", i


t1 = Thread(target=foo)
t2 = Thread(target=bar)

t1.start()

t2.daemon = True
t2.start()

for i in range(5):
    print "In main: counting", i
    sleep(1)

print "Main thread complete..."




