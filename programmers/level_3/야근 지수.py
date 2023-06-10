import heapq
from typing import List

def solution(n: int, works: List[int]) -> int:
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        w = heapq.heappop(works)
        if not w:
            break
        heapq.heappush(works, w+1)
    return sum([w**2 for w in works])
