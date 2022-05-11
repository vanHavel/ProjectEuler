with open('61-70/p067.txt') as f:
    input = f.read()

nums = [[int(s) for s in line.split()] for line in input.splitlines()]
n = len(nums)
for i in range(n-2, -1, -1):
    for j in range(0, i+1):
        nums[i][j] += max(nums[i+1][j], nums[i+1][j+1])
print(nums[0][0])