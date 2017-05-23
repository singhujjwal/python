from __future__ import print_function

from threading import Thread
from time import sleep

def testfn(n):
    for i in range(10):
        #print "In", n, "counting", i
        #print("In", n, "counting", i)
        print("In {}: Counting {}".format(n, i))
        sleep(1)

t1 = Thread(target=testfn, args=("foo",))
t2 = Thread(target=testfn, args=("bar",))
t1.start()
t2.start()
testfn("main")



