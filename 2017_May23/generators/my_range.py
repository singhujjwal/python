def myrange(*args):
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError, "myrange() must be called with 1 to 3 arguments!"

    while start < stop:
        yield start
        start += step



for i in myrange(10): print i,
# 0 1 2 3 4 5 6 7 8 9
print "\n"

for i in myrange(10, 20): print i,
# 10 11 12 13 14 15 16 17 18 19
print "\n"

for i in myrange(10, 20, 2): print i,
# 10 12 14 16 18
print "\n"

