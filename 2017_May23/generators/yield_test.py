def foo():
    print "In foo 1: yielding 10"
    yield 10

    print "In foo 2: yielding 'hello world'"
    yield "hello world"

    return

    print "In foo 3: yielding a tuple"
    yield 10, "hello", 40


for i in foo():
    print "In for loop: i =", i


