#include <stdio.h>
#include <sys/time.h>
#include <math.h>

#define NUM_PRIMES 1000

struct timeval start, end;

int is_prime(long long n) {
    long long i;
    
    long long s = (long long)sqrtl(n) + 1;

    for (i=2; i<s; i++) {
        if ((n%i) == 0) 
            return 0;
    }
    return 1;
}

void gen_primes(int num_primes)
{
    long long i = 2;

    while (num_primes) {
        if (is_prime(i)) { 
            printf("%lld\n", i);
            --num_primes;
        }
        ++i;
    }
}

int main()
{
    printf("Generating first %d prime numbers...\n", NUM_PRIMES);
    gettimeofday(&start, NULL);
    gen_primes(100000);
    gettimeofday(&end, NULL);

    printf("Duration: %d.%d seconds.\n", 
                (int)(end.tv_sec - start.tv_sec),
                (int)(end.tv_usec - start.tv_usec));

    return 0;
}

