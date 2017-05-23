def myrange(start, stop):
    start = 0
    step = 1
    while start < stop:
        yield start
        start += step


for i in myrange(10): print i,
# OUT: 0 1 2 3 4 5 6 7 8 9

for i in myrange(10, 20): print i,
# OUT: 10 11 12 13 14 15 16 17 18 19

