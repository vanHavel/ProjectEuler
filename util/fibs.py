from typing import Iterable

def fibs() -> Iterable[int]:
    prev = 0
    cur = 1
    while True:
        yield cur 
        prev, cur = cur, prev + cur