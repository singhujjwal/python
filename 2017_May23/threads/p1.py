from time import sleep
from multiprocessing import Process

def foo():
    for i in range(5):
        print "In foo: count =", i
        sleep(1)


def bar():
    for i in range(5):
        print "In bar: count =", i
        sleep(1)

p1 = Process(target=foo)
p2 = Process(target=bar)

p1.start()
p2.start()

#t1.join()
#t2.join()
print "Main exiting..."

