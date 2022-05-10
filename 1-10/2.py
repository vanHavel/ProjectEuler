from itertools import takewhile

def fibs():
    prev = 0
    cur = 1
    while True:
        yield cur 
        prev, cur = cur, prev + cur

res = sum(x for x in takewhile(lambda x: x < 4_000_000, fibs()) if x % 2 == 0)
print(res)