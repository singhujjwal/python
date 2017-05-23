from __future__ import print_function
from time import sleep

import threading

def fn(tname, count):
    for i in range(count):
        print("In {} counting {}".format(tname, i))
        print("Active threads: {}".format(threading.active_count()))
        sleep(0.5)

t1 = threading.Thread(target=fn, args=("foo", 10))
t2 = threading.Thread(target=fn, args=("bar", 15))

t1.some_data = "This is foo function..."
t1.start()

t2.some_data = "This is bar function..."
t2.start()

fn("main", 5)

