import itertools

print(next(itertools.islice(itertools.permutations(range(10)), 999_999, None)))