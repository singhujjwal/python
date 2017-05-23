from multiprocessing.connection import Listener
from multiprocessing import Process, Pool
from time import ctime

def handle_connection(conn):
    while True:
        try:
            line = conn.recv_bytes()
        except: 
            break
        #if not line: break
        print "Got line:", line
        conn.send_bytes(line.upper())
    conn.close()

def poll_connection(server):
    while True:
        conn = server.accept()
        handle_connection(conn)


server = Listener(address=("", 6000))

p = Pool(10)
p.apply_async(func=poll_connection, args=(server,))

p.join()


