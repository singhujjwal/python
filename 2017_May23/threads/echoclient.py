from multiprocessing.connection import Client
import sys

conn = Client(address=("", 6000))


while True:
    line = sys.stdin.readline()
    if not line.strip(): break
    conn.send_bytes(line)
    reply = conn.recv_bytes()
    print "Reply: ", reply

conn.close()


