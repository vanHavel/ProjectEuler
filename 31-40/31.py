import functools

sum = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

@functools.lru_cache(maxsize=None)
def ways(n, k):
    ans = 0
    if n < 0 or k < 0: 
        return 0
    if n == 0:
        return 1
    if n >= coins[k]:
        ans += ways(n - coins[k], k)
    ans += ways(n, k-1)
    return ans

print(ways(sum, len(coins)-1))