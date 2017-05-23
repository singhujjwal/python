from multiprocessing.managers import BaseManager

class MathsClass(object):
    def add(self, x, y):
        pass

    def mul(self, x, y):
        pass

class Car(object):
    def drive(self): pass

class MyManager(BaseManager): pass

MyManager.register('Maths', MathsClass)
MyManager.register('Car', Car)

