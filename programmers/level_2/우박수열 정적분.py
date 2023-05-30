from typing import List

def to_one(num: int) -> int:
    if num == 1:
        return [1]
    if num % 2:
        return [num] + to_one(3*num+1)
    return [num] + to_one(num//2)

def solution(k: int, ranges: List) -> List[int]:
    series = to_one(k)
    answer = []
    for s, e in ranges:
        e += len(series)
        if s >= e:
            answer.append(-1)
        else:
            answer.append(sum(series[s:e]) - (series[s] + series[e-1])/2)
    return answer
