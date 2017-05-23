#!/usr/bin/env perl 
use strict;
use warnings;
use Time::HiRes qw/gettimeofday/;

sub is_prime {
    my $v = shift;
    my $s = sqrt($v) + 1;

    for (my $i=2; $i<$s; $i++) {
        return 0 unless ($v % $i);
    }
    return 1;
}

sub gen_prime {
    my $n = shift;
    my $i = 2;

    while ($n) {
        if (is_prime($i)) {
            print $i, "\n";
            --$n;
        }
        ++$i;
    }
}

my $num_primes = 100000;
print "Generating $num_primes prime numbers...\n";

my ($start_sec, $start_usec) = gettimeofday;
gen_prime($num_primes);
my ($end_sec, $end_usec) = gettimeofday;

printf "Duration: %d.%d seconds\n", 
             ($end_sec - $start_sec), 
             ($end_usec - $start_usec);

