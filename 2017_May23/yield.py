import time

my_generator = (x*x for x in range(100))
for i in my_generator:
    print (i)

time.sleep(1)
try:
    for i in my_generator:
        print (i)
except:
    print ("Exception thrown....")


time.sleep(1)

print ("-"*25)

def createGenerator():
    mylist = range(10)
    for i in mylist:
        yield i*i


gen = createGenerator()
print (gen)
for i in gen:
    print (i)

print ("-"*25)



