from util import primes

upper = 10000
ps = primes.sieve(upper)
divsums = [0] + [sum(primes.divisors(n)) - n for n in range(1, upper+1)]
ans = 0
for index, divsum in enumerate(divsums):
    if divsum <= upper and divsum != index and divsums[divsum] == index:
        ans += index
print(ans)