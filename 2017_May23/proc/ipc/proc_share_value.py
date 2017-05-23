from multiprocessing import Process, Value
#from threading import Thread as Process

from time import sleep

num = Value('i', 100)

#class Value:
#    def __init__(self, v):
#        self.value = v

#num = Value(100)

def foo(n):
    print "In foo: v = ", n.value 
    sleep(1)
    n.value = 500
    print "In foo: v now is", n.value


def bar(n):
    print "In bar: v =", n.value
    sleep(2)
    print "In bar: v now is", n.value



p1 = Process(target=foo, args=(num,))
p2 = Process(target=bar, args=(num,))

p1.start()
p2.start()

