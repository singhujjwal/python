from threading import Thread
from time import sleep

class MyThread(Thread):

    def __init__(self, name, count):
        Thread.__init__(self)
        self.name = name
        self.count = count

    def run(self):
        for i in range(10):
            print("In {}, counting {}".format(self.name, self.count))
            sleep(0.5)


t1 = MyThread("foo", 10)
t2 = MyThread("bar", 15)
t1.start()
t2.start()

