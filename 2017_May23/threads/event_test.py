from threading import Thread, Event
from random import random, randint
from time import sleep
from sys import stdout

data = []

updated = Event()

def update_data():
    sleep(5)
    for i in range(10): data.append(randint(1,100))
    updated.set()


def get_data(name):
    while True:
        print("{} waiting for list update...".format(name))
        updated.wait()
        print("In {}: data = {}\n".format(name, str(data)))
        stdout.flush()


update_thread = Thread(target=update_data)

readers = {}

update_thread.start()

for i in range(5):
    readers[i] = Thread(target=get_data, args=("Reader-%d" % i,))
    readers[i].start()


