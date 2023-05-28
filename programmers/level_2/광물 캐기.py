import math
from typing import List

def solution(picks: List[int], minerals: List[str]) -> int:
    """
    Idea
    - 5개씩 나눠서 각 광물의 개수를 count.
    - pick의 수가 부족할 수 있으니 slice.
    - sort후 뒤부터 pop하여 다이아몬드 곡갱이부터 사용.
    """
    counts = []
    # Table
    tir = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    # 5개씩 묶어서 count.
    for i in range(math.ceil(len(minerals)/5)):
        part = minerals[i*5: (i+1)*5]
        counts.append([
            part.count("diamond"),
            part.count("iron"),
            part.count("stone")])
    counts = counts[:sum(picks)]
    # 피로도 오름차순 정렬.
    counts.sort()
    answer = 0
    # 다이아 곡괭이 부터.
    for pick, tir in zip(picks, tir):
        for _ in range(pick):
            if not counts:
                return answer
            # 가장 피로도가 높은 케이스 pop.
            d, i, s = counts.pop()
            answer += tir[0] * d + tir[1] * i + tir[2] * s
    return answer
