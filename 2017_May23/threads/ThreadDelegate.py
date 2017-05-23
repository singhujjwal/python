from threading import Thread
from time import sleep

class ThreadDelegate(Thread):
   def __init__(self, n, target):
      Thread.__init__(self, name=n)
      self.th_name = n
      self.th_target = target

   def run(self):
      self.th_target.run(self)


class MyOwnThread:
   def __init__(self):
      self.count = 0

   def run(self, th):
      while True:
         print "Running from %s, count = %d" % (th.th_name, self.count)
         sleep(1)
         self.count += 1
                
obj = MyOwnThread()
t1 = ThreadDelegate("thread1", obj)
t2 = ThreadDelegate("thread2", obj)

t1.start()
t2.start()
    
