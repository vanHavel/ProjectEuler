from collections import defaultdict
from math import ceil, sqrt
from typing import List, Optional


def sieve(upper: int) -> list[int]:
    primes = [2]
    k = 3
    while primes[-1] < upper:
        prime = True
        for p in primes:
            if p * p > k:
                break
            if k % p == 0:
                prime = False
                break   
        if prime:
            primes.append(k) 
        k += 2
    return primes[:-1]


def prime_factors(n: int, primes: Optional[list[int]] = None) -> dict[int, int]:
    if not primes:
        primes = sieve(n)
    factors = defaultdict(int)
    for p in primes:
        while n % p == 0:
            factors[p] += 1
            n //= p
    return factors