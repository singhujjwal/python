from threading import Thread, local
import random

def out(*s):
    from sys import stdout
    for i in s:
        stdout.write(str(i))
    stdout.write("\n")
    stdout.flush()


mydata = [0, 0, 0, 0]  


def bar(name):
    global mydata
    out("In %s[bar]: mydata = %s" % (name, str(mydata.nums)))

def foo(name):
    global mydata
    mydata = local()
    mydata.nums = random.sample(range(10, 100), 5)[:]
    out("In %s[foo]: mydata = %s" % (name, str(mydata.nums)))
    bar(name)

t1 = Thread(target=foo, args=("thread1",))
t2 = Thread(target=foo, args=("thread2",))

t1.start()
t2.start()

