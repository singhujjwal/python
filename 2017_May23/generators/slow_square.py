def slow_square(x):
    from time import sleep
    sleep(1)
    return x*x

# Generator comprehension
result = ( slow_square(v) for v in range(10) )
print "Result computed!"

for r in result: print r

