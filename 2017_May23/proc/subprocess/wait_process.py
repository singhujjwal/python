#!/usr/bin/env python

from subprocess import Popen
from time import sleep

p = Popen("./slow_program.py")

for i in range(5):
    print "Main program: counting ", i
    sleep(1)

ret = p.wait()
print "Child process exited with exit code", ret


