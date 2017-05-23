import os
from time import sleep
from threading import Thread

class MyThread:
   
   def __init__(self):
      self.count = 0

   def run1(self):
      while True:
          print "In run1: counting %d" % self.count
          sleep(1)
          self.count += 1

   def run2(self):
      while True:
          self.count += 1
          sleep(1)
          print "In run2: counting %d" % self.count
          sleep(1)
          self.count += 1
    
o1 = MyThread()

t1 = Thread(target=o1.run1, name="thread1")
t2 = Thread(target=o1.run2, name="thread2")

t1.start()
t2.start()




        


