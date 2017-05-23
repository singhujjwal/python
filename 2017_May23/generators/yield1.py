def foo():
    print "In foo..."
    yield 100

    print "Back in foo..."
    yield "Hello world"

    
    print "Back again in foo..."
    yield 4.5, 6, 10

    print "End of foo..."

#g = foo()

print "Entering for loop..."

for i in foo():
    print "In for loop: i =", i
    if i == 'Hello world': break

