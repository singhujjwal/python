from multiprocessing.connection import Client

conn = Client(address=("", 6000))

data = conn.recv_bytes()
print data

obj = conn.recv()
print obj

conn.close()

