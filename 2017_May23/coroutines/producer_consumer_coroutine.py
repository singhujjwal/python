from random import randint, random
from time import sleep

# A random number generator
def producer():
    while True:
        value = randint(10, 99)
        print "Producer: generated value %d" % value
        yield value

# A co-routine that consumes value
def consumer():
    count = total = 0
    while True:
        value = yield
        count += 1
        total += value
        print "Consumer: consumed %d, count = %d, total = %d\n" % (value, count, total)
        yield value*value

if __name__ == '__main__':
    p = producer()
    c = consumer()
    next(c)

    for v in p:
        r = c.send(v)
        print "Square of", v, "=", r
        sleep(random())
        next(c)



