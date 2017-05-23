from multiprocessing import Process
from time import sleep
import os

def child_handler():
   for i in range(30):
       print "In child[%d]: counting %d" % (os.getpid(), i)
       sleep(1)


for i in range(5):
    p = Process(target=child_handler)
    p.start()
    print("Pid = ", p.pid)

sleep(15)
print "Main program exited."





