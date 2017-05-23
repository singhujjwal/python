from time import sleep
#from multiprocessing import Process
from threading import Thread as Process
from sys import stdout

i = 0

def foo(name):
    global i
    while True:
        stdout.write("In foo[%s]: counting %d\n" % (name, i))
        sleep(0.5)
        i += 1

p1 = Process(target=foo, args=("process-1",))
p2 = Process(target=foo, args=("process-2",))

p1.start()
p2.start()

