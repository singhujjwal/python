import java.math.*;

class GenPrime {
    public static final long NUM_PRIMES = 100000;

    public static boolean isPrime(long v) {
        long s = ((long)Math.sqrt(v)) + 1;

        for (long i=2; i<s; i++) {
            if ((v%i) == 0)
                return false;
        }
        return true;
    }

    public static void genPrimes(long n) {
        int i = 2;
        
        while (n > 0) {
            if (isPrime(i)) {
                System.out.println(i);
                --n;
            }
            ++i;
        }
    }

    public static void main(String[] args) {
        System.out.printf("Generating %d prime numbers.\n", NUM_PRIMES);

        long start = System.currentTimeMillis();
        genPrimes(NUM_PRIMES);    
        long duration = System.currentTimeMillis() - start;

        System.out.printf("Duration: %d.%d seconds.\n",
                            (duration / 1000), (duration % 1000));
    }

}
