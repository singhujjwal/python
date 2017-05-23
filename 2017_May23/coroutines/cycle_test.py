
a = [10, 20, 30, 40, 50, 60]


#def cycle(coll):
#    i = 0
#    while True:
#        yield coll[i]
#        i += 1
#        if i >= len(coll): i = 0

from itertools import cycle

for i in cycle(a): print(i)

