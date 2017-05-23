from time import sleep
from threading import Thread

def count(name, n):
    for i in range(n):
        sleep(1)
        print "In {}: counting {}".format(name, i)


t1 = Thread(target=count, args=("foo", 10))
t2 = Thread(target=count, args=("bar", 10))

t1.start()
t2.start()

count("main", 5)

t1.join()
print "Thread t1 complete..."

t2.join()
print "Thread t2 complete..."

print "Main thread complete..."




