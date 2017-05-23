from time import sleep

def fibo(x):
    a, b = 0, 1
    for i in xrange(x):
        print a,
        a, b = b, a + b

def fibo_list(x):
    series = [0, 1]
    for i in xrange(x-2):
        series.append(series[-1] + series[-2])
    return series

def fibo_gen(x):
    a, b = 0, 1
    for i in xrange(x):
        yield a
        a, b = b, a + b


#for i in fibo_gen(10):
#    if i == 3: break
#    print i,


