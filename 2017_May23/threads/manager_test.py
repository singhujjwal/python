from multiprocessing.managers import BaseManager

manager = BaseManager(address=("", 6000), authkey="abc")

server = manager.get_server()
server.serve_forever()

