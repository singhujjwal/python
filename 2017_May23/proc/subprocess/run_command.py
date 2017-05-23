from subprocess import Popen
from shlex import split

while True:
    c = raw_input("Enter command: ")
    p = Popen(split(c))
    p.wait()

