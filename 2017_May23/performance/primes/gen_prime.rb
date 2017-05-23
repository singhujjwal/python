def prime?(v)
    s = (v ** 0.5).to_i + 1
    2.upto(s) do |i|
        return FALSE if ((v%i) == 0)
    end
    return TRUE
end

def gen_prime(n)
    i = 2
    while n > 0
        if prime? i
            puts i
            n -= 1
        end
        i += 1
    end
end

num_primes = 100000
puts "Generating #{num_primes} prime numbers"

start = Time.now.to_f
gen_prime(num_primes)
duration = Time.now.to_f - start

puts "Duration: #{duration} seconds."
