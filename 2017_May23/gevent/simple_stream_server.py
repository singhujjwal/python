from gevent.server import StreamServer

def handle(socket, address):
    socket.send("Hello from a telnet!\n")
    while True:
        data = socket.recv(20)
        if "end" in data: break
        socket.send("SERVER SAYS: " + data.upper())
    socket.send("bye!")
    socket.close()

server = StreamServer(('127.0.0.1', 5000), handle)
server.serve_forever()
