

a = 10

def foo():
    global a
    print "In foo: a = ", a
    a = 100
    print "In foo: a = ", a


foo()
print "In main: a = ", a

