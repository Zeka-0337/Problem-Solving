from typing import List

def solution(n: int, s: int) -> List[int]:
    # if s is not dividable by s.
    if n > s:
        return [-1]
    a, b = divmod(s, n)
    return [a] * (n-b) + [a+1] * b
