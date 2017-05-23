import gevent

def testfn(name, count):
    for i in range(count):
        print("In {}, count = {}".format(name, count))
        while True: pass

        gevent.sleep(1)


g1 = gevent.spawn(testfn, "foo", 10)
g2 = gevent.spawn(testfn, "bar", 15)
g3 = gevent.spawn(testfn, "baz", 20)

gevent.joinall([g1, g2, g3])

