from subprocess import Popen, PIPE

#with open("bc.in") as infile:
#    p = Popen("bc", stdin=infile)
#    p.wait()

commands = """
scale=100
sqrt(2)
quit
"""

p = Popen("bc", stdin=PIPE, stdout=PIPE)
p.stdin.write(commands)
p.stdin.close()

for line in p.stdout:
    print "Reading:", line

p.stdout.close()

