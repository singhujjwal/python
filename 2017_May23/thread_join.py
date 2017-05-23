from __future__ import print_function
from time import sleep

from threading import Thread

def fn(tname, count):
    for i in range(count):
        print("In {} counting {}".format(tname, i))
        sleep(0.5)

t1 = Thread(target=fn, args=("foo", 10))
t2 = Thread(target=fn, args=("bar", 1500))

t1.start()

t2.daemon = True
t2.start()

fn("main", 5)

t2.join(10)
if t2.is_alive():
    print("Main: t2 is still running...")
else:
    print("Main: t2 completed...")

t1.join()
if t1.is_alive():
    print("Main: t1 is still running...")
else:
    print("Main: t1 completed...")

print("Main complete...")
