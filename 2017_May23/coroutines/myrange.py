def myrange(*args):
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError, "Invalid arguments: syntax is myrange(start, stop, step)"

    while start < stop:
        yield start
        start += step


print list(myrange(10)) # -> start=0, stop=10, step=1

print list(myrange(10, 20)) # -> start=10, stop=20, step=1

print list(myrange(10, 20, 2)) # -> start=10, stop=20, step=2


