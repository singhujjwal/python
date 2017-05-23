from time import sleep
from threading import Thread

def testfn(name, count):
    for i in range(count):
        print('In {}: count = {}'.format(name, i))
        sleep(1)

if __name__ == '__main__':

    workers = {}
    for i in range(10):
        workers[i] = Thread(target=testfn,
                            args=("woker-{}".format(i), 5))
        workers[i].start()

