def accumulator(start=0):
    total = start
    
    while True:
        value = yield
        if not value: break
        total += value
        yield total
    print total


a = accumulator(10)
a.next()

print a.send(20)
a.next()

print a.send(30)
a.next()

print a.send(40)
a.next()

print a.send(0)
a.next()

