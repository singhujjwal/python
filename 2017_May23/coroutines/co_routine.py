def accumulate(x=0):
    total = x

    while True:
        v = yield
        if v is None: break
        total += v
        #print "Accumulated: ", total

    yield total 


a = accumulate(0)
a.next()
a.send(10)
a.send(20)
a.send(30)
a.send(40)
total = a.next()
print "Total =", total



