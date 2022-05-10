p = 600851475143

div = 3
while True:
    if div * div > p:
        break
    if p % div == 0:
        p //= div 
    else:
        div += 2
print(p)