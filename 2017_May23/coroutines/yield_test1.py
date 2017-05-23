from time import sleep

def foo():
    print "In foo function..."
    yield "hello"
    print "Back into foo function..."
    return
    yield 100
    print "Back again into foo function..."
    yield "this is a test string"

for v in foo():
    print "In main: v =", v



