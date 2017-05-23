from subprocess import PIPE, Popen
from sys import stdout, stdin
from threading import Thread

def send_data(p):
    from sys import stdin
    while True:
        print "bc>",
        data = stdin.read()
        p.stdin.write(data)
        p.stdin.flush()


def recv_data(p):
    while True:
        for line in p.stdout:
            print line,
            stdout.flush()

cmd = Popen(["bc", "-l"], stdout=PIPE, stdin=PIPE)
print "BC started... connecting..."

s = Thread(target=send_data, args=(cmd,))
r = Thread(target=recv_data, args=(cmd,))

s.start()
r.start()

cmd.wait()

