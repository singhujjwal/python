from multiprocessing.connection import Listener
from time import ctime

server = Listener(address=("", 6000), authkey="abc")

while True:
    conn = server.accept()
    print "Got connection from: ", conn
    conn.send_bytes(ctime())
    conn.send(["hello", 34.3, ("john", "sam", "jones")])
    conn.close()

