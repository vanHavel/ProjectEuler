best = 0
for a in range(1000):
    for b in range(1000):
        prod = a * b 
        if str(prod) == str(prod)[-1::-1] and prod > best:
            best = prod 

print(best)