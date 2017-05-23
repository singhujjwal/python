
def style(output):
    def decorate(f):
        if output == "bold":
            def wrap():
                return "<bold>" + f() + "</bold>"
        elif output == "italics":
            def wrap():
                return "<i>" + f() + "</i>"
        return wrap
    return decorate

def bold():
    print "bold() called: "
    def decorate(f):
        print "Decorator called: f = ", f
        def wrap():
            print "Wrapper called"
            return "<bold>" + f() + "</bold>"
        return wrap
    return decorate

@bold()
def greet():
    return "Hello world"


@style(output="italics")
def welcome():
    return "Welcome to Python"


print greet()
print welcome()

