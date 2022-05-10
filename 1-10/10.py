from util.primes import sieve

upper = 2_000_000
primes = sieve(upper)

print(sum(primes))