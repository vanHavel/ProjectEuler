

from typing import Optional


def binomial_coefficients(upper: int) -> list[list[int]]:
    assert upper >= 0 
    res = [[1]]
    for n in range(1, upper+1):
        res.append([1])
        for k in range(1, n):
            res[n].append(res[n-1][k] + res[n-1][k-1])
        res[n].append(1)
    return res

def choose(n: int, k: int, coefficients: Optional[list[list[int]]] = None) -> int:
    assert n >= 0
    assert k >= 0
    assert n >= k
    if not coefficients:
        coefficients = binomial_coefficients(n)
    return coefficients[n][k]

