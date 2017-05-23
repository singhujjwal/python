from multiprocessing.connection import Listener
from multiprocessing import Process
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

server = Listener(address=("", 6000))

while True:
    conn = server.accept()
    Process(target=handle_connection, args=(conn,)).start()  

