with open('21-30/p022.txt') as f:
    names = sorted(f.read().replace('"', '').split(','))

ans = sum(
    (index + 1) * sum(ord(c) - ord('A') + 1 for c in name) 
    for index, name in enumerate(names)
)
print(ans)