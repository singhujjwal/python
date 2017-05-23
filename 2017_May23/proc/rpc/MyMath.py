from multiprocessing.managers import BaseManager

class MathsClass(object):
    def add(self, x, y):
        print "add method called."
        return x + y

    def mul(self, x, y):
        print "mul method called."
        return x * y

class MyManager(BaseManager): pass

MyManager.register('Maths', MathsClass)

if __name__ == '__main__':
    manager = MyManager(address=('127.0.0.1', 5050), authkey="secret") 
    server = manager.get_server()
    server.serve_forever()

#    manager = MyManager(address=('127.0.0.1', 6060), authkey='abcd') 
#    manager.connect()
#    maths = manager.Maths()
#    print maths.add(4, 3)         # prints 7
#    print maths.mul(7, 8)         # prints 56

