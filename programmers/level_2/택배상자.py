from typing import List

def solution(order: List[int]) -> int:
    prev = order[0]
    for idx, o in enumerate(order[1:]):
        if not (o == prev - 1 or o > prev):
            return idx+1
        prev = o
    return len(order)

print(solution([3,5,4,2,1]))
