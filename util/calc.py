from functools import reduce
from typing import Iterable

def product(nums: Iterable[int]) -> int:
    return reduce(lambda x, y: x * y, nums, 1)
    