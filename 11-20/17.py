def write_number(n: int) -> str:
    if n == 1000:
        return "onethousand"
    res = ""
    if n >= 100:
        res += write_number(n // 100) + "hundred"
        if n % 100 != 0:
            res += "and"
    n = n % 100 
    if n >= 20:
        res += ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][n // 10 - 2]
        if n % 10 > 0:
            res += write_number(n % 10)
    elif n >= 11:
        res += ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][n-11]
    elif n > 0:
        res += ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"][n-1]
    return res 

ans = 0
for i in range(1, 1001):
    ans += len(write_number(i))
print(ans)
    