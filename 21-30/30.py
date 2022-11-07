upper = 354294
power = 5
ans = 0
for i in range(2, upper+1):
    cur = i
    dig = 0 
    while cur > 0:
        rem = cur % 10 
        dig += rem ** power
        cur //= 10 
    if i == dig:
        ans += i
print(ans)