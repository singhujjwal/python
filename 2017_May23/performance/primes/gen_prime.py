def is_prime(x):
    s = int(x ** 0.5) + 1
    for i in xrange(2, s): 
        if x % i == 0: return False
    return True

def gen_prime(n):
    i = 2
    while n:
        if is_prime(i):
            print i
            n -= 1
        i += 1

from time import time
num_primes = 100000
print "Generating %d prime numbers..." % num_primes

start = time()
gen_prime(num_primes)
end = time()
print "Duration: ", end - start, "seconds"

