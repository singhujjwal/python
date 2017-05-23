from time import sleep
from threading import Thread
import pdb

def testfn(name, count):
    try:
        for i in range(count):
            if name == "foo" and i > 6:
                raise ValueError("invalid count...")

            print('In {}: count = {}'.format(name, i))
            sleep(1)
    except Exception as e:
        pdb.set_trace()


if __name__ == '__main__':
    t1 = Thread(target=testfn, args=("foo", 10))
    t2 = Thread(target=testfn, args=("bar", 15))

    t1.start()
    t2.start()
    testfn("main", 5)
    t1.join()
    print("Back to main thread: t1 is complete...")
    t2.join()
    print("Back to main thread: t2 is complete...")

