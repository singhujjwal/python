from __future__ import print_function
from time import sleep

from threading import Thread, current_thread

def fn(tname, count):
    th = current_thread()
    for i in range(count):
        if hasattr(th, "cancel") and getattr(th, "cancel") == True:
            break
        print("In {} counting {}".format(tname, i))
        sleep(0.5)

t1 = Thread(target=fn, args=("foo", 10))
t2 = Thread(target=fn, args=("bar", 15))

t1.start()
t2.start()

fn("main", 5)
t1.cancel = True
t1.join()
print("Main: t1 completed...")


sleep(2)
t2.cancel = True
t2.join()
print("Main: t2 completed...")

print("Main complete...")
