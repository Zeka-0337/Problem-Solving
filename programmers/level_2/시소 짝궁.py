from typing import List
from collections import Counter
import math


def solution(weights: List[int]) -> int:
    answer = 0
    case = [4 / 3, 2, 3 / 2]
    weights = Counter(weights)
    for k, v in weights.items():
        answer += math.comb(v, 2)
        for c in case:
            if k * c in weights:
                answer += v * weights[k * c]
    return answer
