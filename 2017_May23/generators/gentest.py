def compute(x):
    from time import sleep
    sleep(1)
    return x*x

a = [10, 20, 30, 40, 50]

print "Computing..."
#b = [ compute(x) for x in a ]

b = ( compute(x) for x in a )

print "Done"
print "Result: ", b
for i in b: 
    print "i = ", i

