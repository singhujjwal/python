from threading import RLock


lock = RLock()

print "Before locking..."
lock.acquire()
print "After locking..."
lock.acquire()
print "After locking again..."

lock.release()
print "Released lock..."

