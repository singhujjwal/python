from time import ctime
from threading import Timer

def foo():
    print("Foo function called at {}".format(ctime()))

t = Timer(5, foo)
t.start()

