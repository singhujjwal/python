from time import sleep
from threading import Thread

class MyThread(Thread):

    def run(self):
        for i in range(10):
            print "i =", i
            sleep(0.5)


t1 = MyThread()
t1.start()

for i in range(10):
    print "In main: i = ", i
    sleep(0.5)

