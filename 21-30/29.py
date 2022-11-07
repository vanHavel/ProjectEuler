upper = 100
nums = {a ** b for a in range(2, upper+1) for b in range(2, upper+1)}
print(len(nums))