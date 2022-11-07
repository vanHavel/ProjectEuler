import itertools 

ans = 0
seen = set()
for perm in itertools.permutations(range(1,10)):
    for a in range(1,4+1):
        for b in range(1, 8-a):
            perm = list(map(str, perm))
            m1 = int("".join(perm[:a]))
            m2 = int("".join(perm[a:a+b]))
            m3 = int("".join(perm[a+b:]))
            if m1 < m2 and m1 * m2 == m3 and m3 not in seen:
                print(m1, m2, m3)
                seen.add(m3)
                ans += m3 
print(ans)
