import math
from typing import List

def solution(n: int, stations: List[int], w: int) -> int:
    answer = 0
    stations = [-w] + stations + [n+w+1]
    for i in range(len(stations)-1):
        empty = stations[i+1] - stations[i] - 2*w - 1
        answer += math.ceil(empty / (2 * w + 1))
    return answer
