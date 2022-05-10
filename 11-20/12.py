from functools import reduce
from util.primes import prime_factors, sieve


acc = 0
primes = sieve(1_000_000)
for i in range(1, 100000):
    acc += i
    fs = prime_factors(acc, primes)
    divisors = reduce(lambda x, y: x * y, [v + 1 for v in fs.values()], 1)
    if divisors > 500:
        break 
print(acc)