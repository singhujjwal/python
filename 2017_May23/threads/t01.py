from time import sleep
from threading import Thread

def foo():
    for i in range(20):
        print "In foo: counting", i
        sleep(0.5)

def bar():
    for i in range(10):
        print "In bar: counting", i
        sleep(0.5)

t1 = Thread(target=foo)
t2 = Thread(target=bar)

#foo()
#bar()

#t1.daemon = True
t1.start()
t2.start()

for i in range(5):
    print "In main: counting", i
    sleep(0.5)

t1.join()
t2.join()
print "Main thread complete..."

