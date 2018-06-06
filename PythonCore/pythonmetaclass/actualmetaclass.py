class LittleMeta(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print("Clsname: ", clsname)
        print("superclass: ", superclasses)
        print("attributedict: ", attributedict)
        return type.__new__(cls, clsname, superclasses, attributedict)
    

class S:
    pass

class A(S, metaclass=LittleMeta):
    pass

# a = A()

x = input("Do you need the answer y/n")
if x.lower() == "y":
    reqiured = True
else:
    reqiured = False

def the_answer(self, *args):
    return 42

class EssentialAnswers(type):
    
    def __init__(cls, classname, superclasses, attributedict):
        if reqiured == True:
            cls.the_answer = the_answer


class Philospher1(metaclass=EssentialAnswers):
    pass

class Philospher2(metaclass=EssentialAnswers):
    pass

class Philospher3(EssentialAnswers):
    pass

plato = Philospher1()
print(plato.the_answer())

kant = Philospher2()
print(kant.the_answer())

# We have learned in our chapter "Type and Class Relationship" 
# that after the class definition has been processed, Python calls
# type(classname, superclasses, attributedict)
# This is not the case if metaclass have been defined in the header
# So the EssentialAnswers will be called instead of type

