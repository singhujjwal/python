#from threading import Thread, Lock
from multiprocessing import Process as Thread, Lock
from time import sleep
from random import random

data_lock = Lock()

def foo(data_lock):
    while True:
        print("Foo trying to acquire data_lock...")
        if data_lock.acquire(2):
            print("Foo acquired lock successfully.")
            sleep(random()*5)
            data_lock.release()
            print("Foo released data_lock...")

def bar(data_lock):
    while True:
        print("Bar trying to acquire data_lock...")
        if data_lock.acquire(2):
            print("Bar acquired lock successfully.")
            sleep(random()*5)
            data_lock.release()
            print("Bar released data_lock...")



t1 = Thread(target=foo, args=(data_lock,))
t2 = Thread(target=bar, args=(data_lock,))

t1.start()
t2.start()


