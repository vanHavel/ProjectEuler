from util import primes 

upper = 28123
ps = primes.sieve(upper)
pset = set(ps)
abunds = {n for n in range(1, upper) if primes.divisorsum(n, ps, pset) - n > n}
nonabundsums = set(range(upper)) - {i+j for i in abunds for j in abunds}
print(sum(nonabundsums))