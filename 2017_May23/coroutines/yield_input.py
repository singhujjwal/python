
def foo():
    print "Inside the co-routine..."
    line = yield

    print "Back to the co-routine..."
    print "In co-routine: line =", line
    yield line.upper()



f = foo()
print "f = ", f

r = f.next()
print "In main: r =", r

r = f.send("this is a test message")
print "In main: r =", r


