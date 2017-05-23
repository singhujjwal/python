from threading import RLock

l = RLock()

print "Program begin"

l.acquire()
print "Lock acquired once"

l.acquire()
print "Lock acquired again"


