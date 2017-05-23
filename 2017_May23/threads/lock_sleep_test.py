from threading import Thread, Lock
from time import sleep

lock = Lock()

def counter(name):
    count = 0
    while True:
        with lock:
            print "{} counting {}".format(name, count)
            sleep(1)
            count += 1
        sleep(0.1)

print "Creating 2 threads..."
foo = Thread(target=counter, args=("foo",))
bar = Thread(target=counter, args=("bar",))

foo.start()
bar.start()

print "Foo and bar started..."

