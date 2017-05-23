#from threading import Thread
from multiprocessing import Process as Thread

from time import sleep

def foo():
    import os
    print("foo function running on: {}".format(os.getpid()))
    sleep(10)
    print("foo function ({}) complete.".format(os.getpid()))


if __name__ == '__main__':
    workers = {}

    for i in range(10):
        workers[i] = Thread(target=foo)
        workers[i].start()

    for i in range(10):
        workers[i].join()

