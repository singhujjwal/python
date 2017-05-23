def sieve_of_eratosthenes():
    from itertools import count 
    non_primes = {}

    for i in count(2):
        n = non_primes.pop(i, None)
        if n is None:
            yield i, non_primes
            non_primes[i*i] = i
        else:
            x = n + i
            while x in non_primes:
                x += n
            non_primes[x] = n


def prime_gen_simple():
    from itertools import count
    for n in count(2):
        for i in xrange(2, int(n ** 0.5)+1):
            if n % i == 0: break
        else:
            yield n

def is_prime():
    while True:
        n = yield
        if n is None: break
        for i in xrange(2, int(n ** 0.5)+1):
            if n % i == 0: 
                yield None
                break
        else:
            yield n

