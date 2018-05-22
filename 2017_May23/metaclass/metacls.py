
'''
@author: ujjwal singh
This is the first python script on the windows.

'''
class ChangeNew(object):

    def __new__(cls, *args, **kwargs):
        print ("Overidding the new method here in class ChangeNew")
        pass

class CheckClass(ChangeNew):

    def __init__(self, name):
        self.name = name
        print("The class is being initialized")

    def kuch(self):
        print("The member function when the object is really used {}".format(self.name))

def main():
    print ("This is the main function")
    cc = CheckClass('Ujjwal')
    # The below line will give code error
    # And the __init__ is not being invoked.
    # cc.kuch()


if __name__ == '__main__':
    main()