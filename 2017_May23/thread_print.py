from time import sleep

from threading import Thread

def fn(tname, count):
    for i in range(count):
        print ("In", tname, "counting", i)
        sleep(0.5)

t1 = Thread(target=fn, args=("foo", 10))
t2 = Thread(target=fn, args=("bar", 15))

t1.start()
t2.start()

fn("main", 5)

