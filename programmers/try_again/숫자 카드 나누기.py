from typing import List
from functools import reduce

def gcd(a: int, b: int) -> int:
    r = a % b
    if not r:
        return b
    return gcd(b, r)

def not_dividable(array: List[int], gcd: int) -> bool:
    for num in array:
        if not num % gcd:
            return False
    return True

def solution(arrayA: List[int], arrayB: List[int]) -> int:
    gcd_a = reduce(lambda x, y: gcd(x, y), arrayA)
    gcd_b = reduce(lambda x, y: gcd(x, y), arrayB)
    gcd_a = gcd_a if not_dividable(arrayB, gcd_a) else 0
    gcd_b = gcd_b if not_dividable(arrayA, gcd_b) else 0
    return max(gcd_a, gcd_b)
