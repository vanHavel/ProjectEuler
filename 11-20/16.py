num = 2 ** 1000
res = 0
while num > 0:
    res += num % 10 
    num //= 10
print(res)