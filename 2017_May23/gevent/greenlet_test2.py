import gevent
from gevent import Greenlet

data = list(range(10))

def square(x):
    gevent.sleep(1)
    data[x] = data[x] ** 2

workers = []
for i in range(10):
    thread = Greenlet.spawn(square, i)
    workers.append(thread)

# Block until all threads complete.
gevent.joinall(workers)

print(data)


