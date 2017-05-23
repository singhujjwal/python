from time import sleep
from multiprocessing import Process, Manager, Condition

def foo(data, c):
    for k, v in data.items():
        data[k] = v.upper()
    with c: c.notify()

def bar(data, c):
    with c: c.wait()
    for k, v in data.items():
        print k, v
    del data["city"]

#d = {}

c = Condition()

m = Manager()
d = m.dict()

d["name"] = "Sam"
d["city"] = "Mumbai"
d["country"] = "India"

p1 = Process(target=foo, args=(d,c))
p2 = Process(target=bar, args=(d,c))

p1.start()
p2.start()

p1.join()
p2.join()

print d
print type(d), d

a = m.list()
a.append(10)
a.append(20)
print a, type(a)
