
'''
@author: ujjwal singh
This is the first python script on the windows.

'''

def testMetaClassWithDecorator():
    x = input("please enter whether you want a answer method or not")
    if x == "y":
        required = True
    else:
        required = False
    # See how the required variable comes into effect
    # Although the good coding practice wants it to be already initialized to 
    # some False value 

    def the_answer(self, *args):
        return 42

    def augument_class(cls):
        if required:
            cls.the_answer = the_answer
        # we have to return this class now
        return cls

    @augument_class
    class Philospher1(object):
        pass

    @augument_class
    class Philospher2(object):
        pass

    @augument_class
    class Philospher3(object):
        pass

    plato = Philospher1()
    kant = Philospher2()

    if required:
        print(kant.the_answer())
        print(plato.the_answer())
    else:
        print("The silence of the philosphers")


# Now what i am testing is that without metaclass also we can add logging and
# tracing to the classes

class BaseClass(object):

    def __new__(cls, *args, **kwargs):
        print ("overriding new in the base class so that every derived\
         clas  have this ")
        return object.__new__(cls, *args, **kwargs)

class DerivedClass(BaseClass):

    def __init__(self):
        pass

    def helper_method(self):
        print ("i am in the helper method of a derived class")


def main():
    print ("This is the main function")
    b = BaseClass()
    print(type(b))

    d = DerivedClass()

    print (type(d))
    d.helper_method()

if __name__ == '__main__':
    main()
    # testMetaClassWithDecorator()