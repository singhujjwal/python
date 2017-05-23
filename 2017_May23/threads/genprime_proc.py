#from threading import Thread
from multiprocessing import Process as Thread

def isprime(x):
    for i in range(2, x-1):
        if x % i == 0: return False
    else:
        return True

def genprimes(x):
    primes = []
    for i in range(2, x):
        if isprime(i): primes.append(i)
    print primes
    #return primes


threads = []
for i in range(10):
    t = Thread(target=genprimes, args=(20000,))
    threads.append(t)
    t.start()

for i in range(10):
    threads[i].join()

