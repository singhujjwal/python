import os
from time import sleep
from threading import Thread

class MyThread(Thread):
   
   def __init__(self, name=None):
      Thread.__init__(self)
      self.count = 0
      self.name = name

   def run(self):
      while True:
          print "In %s: counting %d" % (self.name, self.count)
          sleep(1)
          self.count += 1


o1 = MyThread("thread1")
o2 = MyThread("thread2")

o1.start()
o2.start()

#t1 = Thread(target=o1.run)
#t2 = Thread(target=o2.run)
#t1.start()
#t2.start()




        


