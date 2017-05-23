from time import sleep
from threading import Thread

def testfn(name, count):
    for i in range(count):
        print('In {}: count = {}'.format(name, i))
        sleep(1)


if __name__ == '__main__':
    t1 = Thread(target=testfn, args=("foo", 1000))
    t2 = Thread(target=testfn, args=("bar", 15))

    t1.daemon = True
    t1.start()
    t2.start()
    testfn("main", 5)

    t2.join()
    print("Main program exiting...")
