from multiprocessing.managers import BaseManager
from time import sleep

class MathsClass(object):
    def add(self, x, y):
        print "add method called."
        sleep(4)
        return x + y

    def mul(self, x, y):
        print "mul method called."
        return x * y

class MyManager(BaseManager): pass

MyManager.register('Maths', MathsClass)

if __name__ == '__main__':
    manager = MyManager(address=('127.0.0.1', 6060), authkey="secret") 
    server = manager.get_server()
    server.serve_forever()

