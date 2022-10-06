from typing import Optional

def get_cycle(d: int) -> Optional[int]:
    cur = 1 
    seen = {}
    index = 0
    seq = []
    while True:
        while cur < d:
            cur *= 10 
        if cur % d == 0:
            return None
        if cur in seen:
            return seq[seen[cur]:index]
        seen[cur] = index 
        seq.append(cur // d)
        cur %= d
        index += 1 

bestLen, best = 0, 0
for d in range(1, 1000):
    cycle = get_cycle(d)
    if cycle and len(cycle) > bestLen:
        bestLen = len(cycle)
        best = d 

print(best, bestLen)