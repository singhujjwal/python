def to_upper():
    while True:
        line = yield
        if not line: break
        yield line.upper()


t = to_upper()
next(t)

lines = "This is line 1", "this is line 2", "this is line 3", "this is the end"

for l in lines:
    print (t.send(l))
    next(t)


