#!/usr/bin/env python

from subprocess import Popen
from time import sleep

p = Popen("./slow_program.py")

for i in range(10):
    print "Main program: counting ", i
    sleep(1)

