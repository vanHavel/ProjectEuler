from collections import defaultdict
from math import ceil, sqrt
from typing import List, Optional

from util import calc

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


def prime_factors(n: int, primes: Optional[list[int]] = None, primeset: Optional[set[int]] = None) -> dict[int, int]:
    assert n > 0
    if not primes:
        primes = sieve(n)
    if primeset and n in primeset:
        return {n: 1}
    factors = defaultdict(int)
    for p in primes:
        while n % p == 0:
            factors[p] += 1
            n //= p
    return factors

def divisors(n: int, primes: Optional[list[int]] = None) -> list[int]:
    factors = prime_factors(n, primes)
    
    def _recurse(_factors: dict[int, int]) -> list[int]:
        if not factors:
            return [1]
        top, cnt = _factors.popitem()
        rec = _recurse(_factors)
        return [top ** pow * rfac for pow in range(cnt+1) for rfac in rec]

    return _recurse(factors)

def divisorsum(n: int, primes: Optional[list[int]] = None, primeset: Optional[set[int]] = None) -> int:
    factors = prime_factors(n, primes, primeset)
    return calc.product((p ** (k+1) - 1) // (p - 1) for p, k in factors.items())
