from threading import RLock

l = RLock()

print "Line 1"
l.acquire()
print "In critical region"
l.acquire()
print "In nested critical region"
l.release()
print "Out of nested critical region"
l.release()
print "Out of critical region"

