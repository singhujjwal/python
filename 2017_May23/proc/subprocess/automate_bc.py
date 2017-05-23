from subprocess import PIPE, Popen
from time import time

cmd = Popen(["bc", "-l"], stdout=PIPE, stdin=PIPE)

start = time()
cmd.stdin.write("scale=2000\n")
cmd.stdin.write("4*a(1)\n")
cmd.stdin.close()
cmd.wait()
end = time()

for line in cmd.stdout:
    print line,


print "Duration: %f seconds" % (end - start)
