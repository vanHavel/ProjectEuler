upper = 1_000_000
lengths = {1: 1} 
for i in range(2, upper+1):
    l = 1
    cur = i
    while cur != 1:
        l += 1
        if cur % 2 == 0:
            cur //= 2 
        else:
            cur *= 3 
            cur += 1
        if cur < i:
            l += lengths[cur] - 1
            break
    lengths[i] = l

best = max(lengths.items(), key=lambda x: x[1])[0]
print(best)