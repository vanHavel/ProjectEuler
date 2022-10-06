from util import primes

primes = set(primes.sieve(1_000_000))
best, bestLen = None, 0
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        cur = 0
        while cur * cur + a * cur + b in primes:
            cur += 1 
        if cur > bestLen:
            bestLen = cur 
            best = (a, b)

ra, rb = best 
print(ra * rb, bestLen)