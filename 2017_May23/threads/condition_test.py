from threading import Thread, Condition
from random import random, randint
from time import sleep

data = []
update = Condition()

def update_data():
    while True:
        sleep(random() * 5)
        with update:
            for i in range(10):
                data.append(randint(1,100))
            update.notifyAll()


def get_data(name):
    while True:
        with update:
            sleep(random())
            update.wait()
            print "In {}: data = {}\n".format(name, str(data))


update_thread = Thread(target=update_data)

readers = {}

update_thread.start()

for i in range(5):
    readers[i] = Thread(target=get_data, args=("Reader-%d" % i,))
    readers[i].start()


