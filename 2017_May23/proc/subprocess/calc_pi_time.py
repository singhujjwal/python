#!/usr/bin/env python
from subprocess import Popen, PIPE
from time import time

calc_pi = """
scale=2000
4*a(1)
quit
"""

p = Popen(["bc", "-l"], stdin=PIPE, stdout=PIPE)
start = time()
p.stdin.write(calc_pi)
p.wait()
end = time()

print "Duration to calculate PI: %f seconds" % (end - start)
 

