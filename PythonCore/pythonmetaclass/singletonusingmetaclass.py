class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs
            )
        return cls._instances[cls]
    
class SingletonClass(metaclass=Singleton):
    pass

class RegularClass():
    pass

x = SingletonClass()
y = SingletonClass()

print (x == y)

x = RegularClass()
y = RegularClass()

print (x == y)

class SingletonBaseWithInheritance(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

class SingletonClassWithInheritance(SingletonBaseWithInheritance):
    pass

x = SingletonClassWithInheritance()
y = SingletonClassWithInheritance()

print (x == y)

x = RegularClass()
y = RegularClass()

print (x == y)